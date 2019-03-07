from django.shortcuts import render, HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.


@csrf_exempt
def show(request,):
    if request.method != "POST":
        return render(request, 'show/scuec.html')
    else:
        get_data = request.POST
        print(get_data['str'])
        result = models.ksxx.objects.filter(bkh__exact=get_data["zkzh"], zjhm__exact=get_data["zjhm"])
        if not result.exists():
            return HttpResponse("输入信息有误或者不存在")
        else:
            data = json.loads(serializers.serialize('json', result))
            return HttpResponse(data[0]['fields'])


@login_required  # 函数访问需要登陆
def login_test(request,):
    if request.user.is_authenticated:  # 检测访问者是否认证过
        return HttpResponse('认证成功')
    else:
        return HttpResponse('认证失败')


def api(request, ):
    url = 'http://apis.scuec.edu.cn/2018/10/10'
    head = {u'appId': u'c39050c629182d6a', u'accessToken': u'7071af6d430db67e000103a2247f05ee', u'content_type': u'application/json'}
    # Content = {u"DWDM": u'all'}
    ret = requests.post(url, headers=head, timeout=10)
    return HttpResponse(ret.text)


