from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse
from kubernetes import client, config
from rest_framework.decorators import api_view

# def index(request):
#     config.load_kube_config()
#     v1 = client.CoreV1Api()
#     print("Listing pods with their IPs:")
#     ret = v1.list_pod_for_all_namespaces(watch=False)
#     for i in ret.items:
#         demo=print("%s\t%s" % (i.metadata.namespace, i.metadata.name))
#         return HttpResponse(demo)

# Configs can be set in Configuration class directly or using helper utilitys
@api_view(['GET'])
def getpods(request):
    if request.method == 'GET':
        #config.load_kube_config()
        #print(request.body.decode["cert"])
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['content']
        print(content)
        #token = "eyJhbGciOiJSUzI1NiIsImtpZCI6InFEbXJQNlpwakdYdjRrU2RWSkFFNVo0UGZCSFpfeVQ1bFlEWVYtSWJuVWsifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZXZvcHMtdG9vbHMiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlY3JldC5uYW1lIjoiYXBpLXNlcnZpY2UtYWNjb3VudC10b2tlbi1sN3N2biIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJhcGktc2VydmljZS1hY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiYzQyZWNmNzktZTFmYS00ZGI0LWI2ZGMtNTg0NjgwYjM4YzAxIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRldm9wcy10b29sczphcGktc2VydmljZS1hY2NvdW50In0.SqdtC9IHIUNj1D6y1L_4imdYiNa-qyP498y4HjggmJP7O45R7j4apiuXG5Dh9Bfrs4ymTojeC9Z496H-IqVGqhZoARGlTftnIgmU7_PIbaETut4PmwalC076jCnv4XSt8k09aY-MoXSuYfSRtuXKMS-1hYrOzy9W5bsaRbZza5H9wpKE06ScV3-WlWXhpx0j-u26zy542WRODcHAYp-MgMouCvGkeMRzb4iY-0TMeL1xUwCV_AL0k0U-WVdlhizQRdnDlPfoP_hhIG_yP-KzfFIXIxVaYLnTsm1jWEixE3cqrgEHB43vq2L56umHxtmeSnwQhdiQH8tixZPpb51o-g"
        configuration = client.Configuration()
        configuration.host = request.GET['api_server']
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": request.META.get('HTTP_AUTHORIZATION')}
        apiClient = client.ApiClient(configuration)
#         configuration = client.Configuration()
# # Configure API key authorization: BearerToken
#         configuration.api_key['authorization'] = 'eyJhbGciOiJSUzI1NiIsImtpZCI6InFEbXJQNlpwakdYdjRrU2RWSkFFNVo0UGZCSFpfeVQ1bFlEWVYtSWJuVWsifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZXZvcHMtdG9vbHMiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlY3JldC5uYW1lIjoiYXBpLXNlcnZpY2UtYWNjb3VudC10b2tlbi1sN3N2biIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJhcGktc2VydmljZS1hY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiYzQyZWNmNzktZTFmYS00ZGI0LWI2ZGMtNTg0NjgwYjM4YzAxIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRldm9wcy10b29sczphcGktc2VydmljZS1hY2NvdW50In0.SqdtC9IHIUNj1D6y1L_4imdYiNa-qyP498y4HjggmJP7O45R7j4apiuXG5Dh9Bfrs4ymTojeC9Z496H-IqVGqhZoARGlTftnIgmU7_PIbaETut4PmwalC076jCnv4XSt8k09aY-MoXSuYfSRtuXKMS-1hYrOzy9W5bsaRbZza5H9wpKE06ScV3-WlWXhpx0j-u26zy542WRODcHAYp-MgMouCvGkeMRzb4iY-0TMeL1xUwCV_AL0k0U-WVdlhizQRdnDlPfoP_hhIG_yP-KzfFIXIxVaYLnTsm1jWEixE3cqrgEHB43vq2L56umHxtmeSnwQhdiQH8tixZPpb51o-g'
# # Uncomment below to setup prefix (e.g. Bearer) for API key, i
#         configuration.api_key_prefix['authorization'] = 'Bearer'
#         configuration.ssl_ca_cert = "/home/knoldus/Desktop/ca.crt"

# # Defining host is optional and default to http://localhost
        # configuration.host = "https://192.168.49.2:8443"
        v1 = client.AppsV1Api(apiClient)
        ret = v1.list_replica_set_for_all_namespaces(watch=False)
        data={}
        data2=[]
        for i in ret.items:
            # data["name"] = i.metadata.name
            # data["namepsace"] = i.metadata.namespace
            data={
                "name": i.metadata.name,
                "namespace": i.metadata.namespace
            }
            data2.append(data)
            #print(data2)
        return HttpResponse(json.dumps(data2, indent=4))



# [
#     {
#         "name": <name>,
#         "namespace"": <ns>
#     }
# ]