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


def main(out_path,type,count):
    with open("configs/icp.json", encoding="utf-8") as fp:
        demo_config = json.load(fp)


    demo_factory = CaptchaFactory(char_custom_fns=[custom_fn], bg_custom_fns=[bg_custom_fn], **demo_config)
    for i in range(1,count+1):
        captcha = demo_factory.generate_captcha()
        captcha.save("%s/%s/%s.jpg" % (out_path, type,i))

        with open('%s/%s.txt'%(out_path,type),'a',encoding='utf-8') as f:
            f.write('%s/%s.jpg\t%s\n'%(type,i,captcha.text))




if __name__ == "__main__":
    out_path = input('请输入输出路径：')
    main(out_path,'train',320000)
    main(out_path,'test',80000)
    main(out_path,'hand',10)
    # print(string.ascii_lowercase)
