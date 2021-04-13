
def postmes(token,ide):
    Url="https://qyapi.weixin.qq.com/cgi-bin/linkedcorp/message/send?access_token={}".format(token)
    data={"touser" :" @all",
          "toparty" :"",
          "totag":"@all",
          "toall":1,
          "msgtype" : "file",
          "agentid" :1000002,
          "file" : {
          "media_id": str(ide)
           },
         "safe":0,
         "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    data3={
   "touser" : "UserID1|UserID2|UserID3",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "voice",
   "agentid" : 1,
   "voice" : {
        "media_id" : "MEDIA_ID"
   },
   "enable_duplicate_check": 0,
   "duplicate_check_interval": 1800
}

    data2={
    "agentid":1000002,
    "allow_user":["zhansan","lisi"],
    "allow_party":[1,2,3],
    "allow_tag":[1,2,3]}
    url2="https://qyapi.weixin.qq.com/cgi-bin/message/get_statistics?access_token={}".format(token)
    print()
    print(requests.post(url=Url,data=data3).text)
    # print(requests.post(url=url2).text)



token="yXNCOHjTCf20TuourGaVVnAFMewXwK6CISB0OuVh4yLzuoovl8gZqyM7WSoTAsg5vK6cNWYR81tD2hOm1rJJe-fnKWb7PNaC4SmoXG9JpISNVANWeznYFWCh0OzCcQQW1BzX-w27vnmNdIxyBVZVU1s6z5s_e68cCRRNquog4dDex0KNwX-E1jjJ4mKBLGNbezfdIqmVdZ5ko6dUWiCpCw"
# print(token)
ide=uploadimg("1.png",token)
postmes(token,ide)

