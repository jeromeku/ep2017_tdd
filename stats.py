from tdd import rest_service as rs
from tdd import stats

s = stats.DataStats()

print(s.stats(rs.RestService().list().values(), 20, 20000))
