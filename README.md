# GPT3.5-api-plugin-for-Stable-Diffusion-Webui
### My intention to create this plugin is because current there is no other plugins can act as a small widget in Stabel Diffusion WebUI
Main function of this plugin is to give you access to Chatgpt 3.5 using API built-in. I have completed basic functionalities.

![Demo](https://github.com/Wangshengyang2004/GPT3.5-api-plugin-for-Stable-Diffusion-Webui/blob/main/example.png)

Above the what the interface look like. You can further develop these two textboxs. For example, fix the system textbox to a give prompt. This may be helpful if you want to nail down a workflow.

# How to use
1. Clone this repo to the extension folder of your Stable Diffusion Webui.
```
#In Terminal
cd /path/to/your/stable-diffusion-webui/extensions
git clone https://github.com/Wangshengyang2004/GPT3.5-api-plugin-for-Stable-Diffusion-Webui.git
```

2. Go to scripts folder, edit config_private.py, replace the key with your GPT3.5 key
* You may also need to edit the stable-webui-gpt3.5api.py to set the http_proxy and https_proxy if you're in network-restrictioned regions like mainland China. Otherwise you will only get timeout result :(
3. You can launch your webui. The plugin will appear on your WebUI.


# Credit to ...
I'm just a beginner in coding, so I have to absorb some useful coding example from others' coding. Thanks to these two projects, I learned a lot from you :)
https://github.com/Rituraj-commits/ChatGPT-Gradio
https://github.com/imrayya/stable-diffusion-webui-Prompt_Generator
