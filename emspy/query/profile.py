import pandas as pd
from .query import Query

'''
A class for profile queries using the EMS REST API
'''


class Profile(Query):
    def __init__(self, conn, ems_name, profile_number, profile_name=''):
        Query.__init__(self, conn, ems_name)
        self._conn = conn
        self._ems_name = ems_name
        self._input_profile_number = profile_number
        self._guid = None
        self._glossary = None
        self._events_glossary = None
        self._input_profile_name = profile_name
        self._ems_id = self.get_ems_id()
        self._search()

    def get_glossary(self):
        if self._guid is not None:
            resp_h, dict_data = self._conn.request(uri_keys=('profile', 'glossary'),
                                                   uri_args=(self._ems_id, self._guid))
            a = pd.DataFrame.from_dict(dict_data)
            # convert the dictionaries values within the glossaryItems column of a into a new DataFrame
            b = a['glossaryItems'].apply(pd.Series)
            # concatenate a and b, drop the old glossaryItems column name
            c = pd.concat([a, b], axis=1).drop('glossaryItems', axis=1)
            self._glossary = c
            return self._glossary
        else:
            print("The search results did not return a profile matching the input profile name and number on the given"
                  "system.  Please try to instantiate the profile object with different arguments.")
            return

    def get_events_glossary(self):
        if self._guid is not None:
            resp_h, dict_data = self._conn.request(uri_keys=('profile', 'events'),
                                                   uri_args=(self._ems_id, self._guid))
            a = pd.DataFrame(dict_data)
            a.set_index('id', inplace=True)
            self._events_glossary = a
            return self._events_glossary
        else:
            print("The search results did not return a profile matching the input profile name and number on the given"
                  "system.  Please try to instantiate the profile object with different arguments.")
            return

    def get_profile_results(self, flight_id):
        raise NotImplementedError
        if self._guid is not None:
            resp_h, dict_data = self._conn.request(uri_keys=('profile', 'profile_results'),
                                                   uri_args=(self._ems_id, flight_id, self._guid))
            '''
            TODO: Implement some sort of parsing of resulting data.  Honestly, it's not super useful unless paired
            with some supplementary information.  There are no names.  No descriptions.  Perhaps I could combine this
            information with the information obtained in the "glossary" and create a meaningful output.   
            
            Glossary, however, does not contain the names and ID's of events.  Maybe those will have to be grabbed using
            the other API endpoints.  
            '''
        else:
            print("The search results did not return a profile matching the input profile name and number on the given"
                  "system.  Please try to instantiate the profile object with different arguments.")
            return

    def _search(self):
        resp_h, dict_data = self._conn.request(uri_keys=('profile', 'search'), uri_args=self._ems_id,
                                               body={'search': self._input_profile_name})
        a = pd.DataFrame.from_dict(dict_data)
        self._search_results = a
        # search for the provided profile number within the returned dataframe
        filtered = a.loc[a['localId'] == self._input_profile_number]
        if len(filtered) == 1:
            print('Found a profile with the supplied profile number and name.')
            self._guid = filtered['id'].values[0]
            self._current_version = filtered['currentVersion'].values[0]
            self._library = filtered['library'].values[0]
            self._profile_name = filtered['name'].values[0]
            self._local_id = filtered['localId'].values[0]
            print('Profile name: {0}, profile number: {1}.'.format(self._profile_name, self._local_id))
        elif len(filtered < 0):
            print(
                'No profile found with the supplied profile number and name.  Perhaps try without the name (it could'
                ' take longer).')
        elif len(filtered > 1):
            print('Somehow found multiple profiles with the supplied name and number.')
