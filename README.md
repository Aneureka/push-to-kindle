# PUSH TO KINDLE!

![](<https://img.shields.io/badge/author-aneureka-orange.svg>) ![AUR license](https://img.shields.io/aur/license/yaourt.svg) [![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

`PUSH TO KINDLE!` 是一个简洁优雅的 Kindle 文档推送工具，快来拯救你的泡面板吧！

## 开始

访问：https://tokindle.top

推送文档到你心爱的 Kindle 上吧~



## 有用吗？

其实通过官方的方法，用邮箱发送文档没什么问题，但因为懒，想去掉重复无谓的操作。



## 技术栈

- JQuery（前端就是一把梭）

- Flask

- Redis Queue（用于异步推送，用 Supervisor 管理）



## 部署

如果你想学习或重新运行本项目，也可以将 `PUSH TO KINDLE!` 部署到你的服务器上，只需要重新填写配置信息：

- 在项目文件夹创建 virtualenv Python3 环境，命名为 venv
- 安装项目依赖： `pip3 install -r requirements`
- 修改 `config.py` （需要注册并配置 [Mailgun](https://www.mailgun.com/) ）
- 将 `run.sh.example` 重命名为 `run.sh` ，并修改它
- 配置 supervisor 将 rq 运行起来，可参考 [官方文档](http://python-rq.org/patterns/supervisor/)
- 运行 `bash run.sh` 启动你的项目吧~



## 感谢

- [filepond](https://github.com/pqina/filepond)，一个超好用又好看的 JS 文件上传工具

- [eruda](https://github.com/liriliri/eruda)，一个移动端网页控制台，用它调试解决了关键的问题



## 捐赠

如果你觉得 `PUSH TO KINDLE!` 挺好用，可以考虑某宝请我喝热水，要恰饭的嘛~

<img width="200px" src="https://i.loli.net/2019/04/07/5ca9ef413e986.jpg" />

