# coding: utf-8

"""
target captcha url: http://www.miitbeian.gov.cn/getVerifyCode?4
"""
import json
import string

from model.capthafactory import CaptchaFactory


def custom_fn(single_char):
    # do something
    # return single_char.filter(ImageFilter.GaussianBlur)
    return single_char


def bg_custom_fn(bg):
    # do something
    # return bg.filter(ImageFilter.GaussianBlur)
    return bg


def main(type,count):
    project_name = "icp"
    with open("configs/icp.json", encoding="utf-8") as fp:
        demo_config = json.load(fp)


    demo_factory = CaptchaFactory(char_custom_fns=[custom_fn], bg_custom_fns=[bg_custom_fn], **demo_config)
    for i in range(1,count+1):
        captcha = demo_factory.generate_captcha()
        captcha.save("output/%s/%s/%s.jpg" % (project_name, type,i))

        with open('output/%s/%s.txt'%(project_name,type),'a',encoding='utf-8') as f:
            f.write('%s/%s.jpg\t%s\n'%(type,i,captcha.text))




if __name__ == "__main__":
    main('train',32000)
    main('test',8000)
    main('hand',10)
    # print(string.ascii_lowercase)
