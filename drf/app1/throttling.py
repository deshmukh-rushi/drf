from rest_framework.throttling import UserRateThrottle



class CityRateThrottle(UserRateThrottle):
     scope = 'city'