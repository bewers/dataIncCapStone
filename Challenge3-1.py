
# coding: utf-8

# In[9]:

import geopy
from geopy.geocoders import GeocoderDotUS
from geopy.geocoders import Nominatim
geolocator = Nominatim()
address, (latitude,longitude) = geolocator.geocode('2408 Pleasant Rose Circle')
print(address,latitude,longitude)


# In[7]:




# In[ ]:



