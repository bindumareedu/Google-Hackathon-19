

from sightengine.client import SightengineClient
api_user = '737578295'
api_secret = 'Us7NTD8APM2ZzUZJtiVA'
image_path = 'pic3.jpeg'

def nudity_shodhuya(api_user,api_secret,image_path):


	client = SightengineClient(api_user,api_secret)

	output = client.check('nudity').set_file(image_path)

	print(output)

	return output

#output1= client.check('nudity').set_bytes(binary_image)
#print(output1)

nudity_shodhuya(api_user,api_secret, image_path)