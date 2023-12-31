import requests, json, re, time, urllib.request


from PIL import Image
import os
 
def combine_imgs_pdf(folder_path, pdf_file_path):
    """
    合成文件夹下的所有图片为pdf
    Args:
        folder_path (str): 源文件夹
        pdf_file_path (str): 输出路径
    """
    files = os.listdir(folder_path)
    png_files = []
    sources = []
    for file in files:
        if 'png' in file or 'jpg' in file:
            png_files.append(folder_path + file)
    png_files.sort()
    output = Image.open(png_files[0])
    png_files.pop(0)
    for file in png_files:
        png_file = Image.open(file)
        if png_file.mode == "RGB":
            png_file = png_file.convert("RGB")
        sources.append(png_file)
    output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)
    


def getParameter(url):  # 获取文档参数
    text_response = requests.get(url=url, headers=headers).text
    actual_page = int(re.search('actual_page: (\d+), //真实页数', text_response).group(1))  # 页数
    aid = re.search('aid: (\d+), //解密后的id', text_response).group(1)  # aid
    view_token = re.search('view_token: \'(.*?)\'', text_response).group(1)  # view_token
    print('actual_page:', actual_page, '\naid:', aid, '\nview_token:', view_token)
    return actual_page, aid, view_token


def requests_data(parameter, page):  # 请求数据
    url = 'https://openapi.book118.com/getPreview.html'
    params = {
        'project_id': '1',
        'aid': parameter[1],
        'view_token': parameter[2],
        'page': page,
    }
    response = requests.get(url=url, headers=headers, params=params).text
    json_data = re.search('jsonpReturn\((.*?)\);', response).group(1)  # 使用正则表达式所需数据
    data = json.loads(json_data)['data']
    # if data.get(str(page)) == '':  # 根据需求使用
    #     print('数据加载失败，重新发出请求')
    #     time.sleep(1)
    #     return requests_data(parameter, page)
    # time.sleep(1)
    return get_data(data)


def get_data(data):  # 下载数据
    for i in data.items():  # i[0]为页数，i[1]为网址
        img_url = 'https:' + i[1]
        urllib.request.urlretrieve(url=img_url, filename=r'D:/doc/image/{}.png'.format(i[0]))  # 下载图片
        print(i[0], img_url)


if __name__ == '__main__':
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    # text_url = "https://max.book118.com/html/2023/0505/8120042035005064.shtm"
    # parameter = getParameter(text_url)
    # for page in range(1, parameter[0], 6):
    #     requests_data(parameter, page)
    
    folder = r"D:\doc\image\\"
    pdfFile = r"D:\doc\pdf\1.pdf"
    combine_imgs_pdf(folder, pdfFile)
