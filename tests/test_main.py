from fastapi.testclient import TestClient


from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
    {
        "name":"c2",
        "breed": "Angora",
        "location_of_origin": "Thailand",
        "coat_length": "short",
        "body_type": "fat",
        "pattern": "blue eyes",
    }

    ] 


def test_post_cat():
    response = client.post(
        "/",
        json = 
            {
                "name":"c2",
                "breed": "Angora",
                "location_of_origin": "Thailand",
                "coat_length": "short",
                "body_type": "fat",
                "pattern": "blue eyes",

            }        
            
    )
    assert response.status_code == 201
    assert response.json() == {"id":1}



def test_put_cat():
    response = client.put(
        "/id",
        json = [
            {
                                           
                "name":"c2",
                "breed": "Angora",
                "location_of_origin": "Thailand",
                "coat_length": "short",
                "body_type": "fat",
                "pattern": "blue eyes",
        }
            ]
                           
         
    )
    assert response.status_code == 201
    assert response.json() == {'id':1}


def test_delete_cat():
    response = client.delete("/id")
    assert response.status_code == 200
    assert response.json().get("id")
    
    
       
   


    
    
    

