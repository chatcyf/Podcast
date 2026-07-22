# Podcast - 陈一发儿的播客工具


## 苹果手机使用部分

苹果手机可以直接用自带的 播客 Podcast 这个工具，打开，播客 - 资料库，通过URL关注节目

之后依次添加下面的url

### 录音室版的音乐

https://www.chatcyf.com/static/podcast/chatcyf.xml

### 斗鱼时期的部分精选

https://www.chatcyf.com/static/podcast/dyvoice.xml

### 茶话会时期的歌曲部分

https://www.chatcyf.com/static/podcast/songs.xml

### 视频部分

https://www.chatcyf.com/static/podcast/videos.xml

## 安卓手机使用部分

安卓手机可以找个类似app就行，比如 AntennaPod 或者 Podcast Go 或者 Moon.fm 之类的

https://github.com/AntennaPod/AntennaPod/releases

https://play.google.com/store/apps/details?id=sanity.podcast.freak

https://moon.fm/

使用方法都差不多

***************************************************************************

## RSS的制作部分

可以直接使用第三方程序部署后，自己搭建播客，然后程序会自动输出xml

比如 Castopod 这种php搭建版，又或者 Selfhost Podcasting 这种wordpress的插件版，太多了，直接搜 podcast 个人搭建，一大堆选项

接下说一下手动生成 .xml 的部分

可以参考上面的xml链接中的内容，修改标题部分，然后对内容部分进行手动替换就行

我是用的 generate_items_all.py 这个脚本，自动扫描生成的媒体链接，最后手动粘贴过去的文本合成的 .xml

可以看看源码参考一下

***************************************************************************

## YouTube的同步部分

去 YouTube Studio 的后台，内容 - 播客 - 新建播客 - 提交 RSS Feed 订阅

之后添加自己的 .xml 链接就行

例如

https://www.youtube.com/playlist?list=PLBI4x3CAi-Oc

https://music.youtube.com/playlist?list=PLBI4x3CAi-Oc

https://www.youtube.com/@chatcyf/podcasts

***************************************************************************
