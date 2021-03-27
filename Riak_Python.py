#pierw musimy zainstalować pakiet "riak" do Pythona (<=3.6)
#pip install riak

import riak

client = riak.RiakClient(port=8098)
user_bucket = client.bucket('s20369')

new_user = user_bucket.new('tonny_info', data={
	"names": {"first_name": "Tonny", "last_name": "Montana"}, 
	"dogs":["Killer", "Coco"], 
	"visits_no": 1, 
	"sex": "Male"
})
new_user.store()

tonny_info = user_bucket.get("tonny_info")
tonny_info.data

modified_user = user_bucket.new('tonny_info', data={
	"names": {"first_name": "Tonny", "last_name": "Montana-Kowalski"}, 
	"dogs":["Killer", "Coco", "Pimpek", "Burek"], 
	"visits_no": 1, 
	"sex": "Male"
})
modified_user.store()

tonny_info_modified = user_bucket.get("tonny_info")
tonny_info_modified.data

user_bucket.delete("tonny_info")
tonny_info_deleted = user_bucket.get("tonny_info")
tonny_info_deleted.data
#Powyższa komenda nic nie zwraca, ale obiekt tonny_info_deleted jest wciąż obiektem typu: 'riak.riak_object.RiakObject' 