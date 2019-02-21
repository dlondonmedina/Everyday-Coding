```python
import pytest

from microblog import app 

@pytest.fixture
def client():
   client = app.test_client()

   yield client 


def test_hello_world(client):
   """ Start to see if we get Hello World back"""

   rv = client.get('/')
   rv2 = client.get('/index')
   assert b'Hello, World!' in rv.data 
   assert b'Hello, World!' in rv2.data
```
