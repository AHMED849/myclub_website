import requests
from django.http import JsonResponse

def get_access_token(request):
    consumer_key = "gkxNFoWRYJG8yASWipdOcF4MaZF15gpHI93V9R7fbYflWph7"
    consumer_secret = "rRzshcAUZTOTI1kE1rRSDYHSdoLS9YAAeG29zQly9yfQwfuI0YCGLThoKGndV2nd"
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_creditentials'
    headers = {'Content-Type': 'application/json'}
    auth = (consumer_key, consumer_secret)
    try:
        response = requests.get(access_token_url, auth=auth, headers=headers)
        response.raise_for_status()
        result = response.json()
        access_token = result('access_token')
        return JsonResponse({'access_token': access_token})
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})
