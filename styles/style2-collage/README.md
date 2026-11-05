# 风格2：杂志手账拼贴

版本 v2 · 配置 [`style.json`](style.json) · 参数：3:4、2K、`prompt_extend=false`

拼接顺序见 `style.json` 的 `template`；② 内容（主标题、副标题、产品、卖点）按根目录 README「规则」填写。

## ① 固定风格

```
小红书竖版冰箱种草封面海报，3:4。视觉风格：杂志手账拼贴风，像把实物纸片贴在桌面上俯拍；配色固定为奶黄、米灰、黑三色，只允许极少量点缀色；素材模块为网格纸、撕边纸、牛皮纸、半透明纸胶带、便签、手绘箭头和圆形色块；纸张有真实的纤维纹理、撕边、轻微褶皱和柔和投影；主标题为黑色超粗黑体；辅助文字为黑色粗体；产品为高清抠图，正面平视，棚拍质感，边缘干净，有轻微投影；整体干净、有层次、留白适度，不杂乱，文字清晰准确，高清。
```

## ③ 随机项（每类抽一项）

| 类别 | 选项 |
|---|---|
| 纸张底 | 1. 米灰色网格纸作底，叠一层撕边牛皮纸<br>2. 有轻微褶皱的米灰色网格纸作底，画面下方约三分之一换成浅灰色点阵纸，交界处为撕边<br>3. 米灰色网格纸作底，左侧露出一条带方形孔的牛皮纸边，像撕下的笔记本页<br>4. 米灰色网格纸作底，顶部斜压一条空白撕边白纸条，右下角叠一片牛皮纸 |
| 标题处理 | 1. 主标题分成两行，每行压在一块独立的奶黄色圆角色块上<br>2. 主标题压在一条横贴的奶黄色宽纸胶带上<br>3. 主标题每个字剪成一块小方纸片拼贴，纸片为奶黄、白、牛皮纸色交错，字均为黑色<br>4. 主标题直接写在纸上，字的下半部压一道奶黄色马克笔高亮 |
| 标题大小 | 1. 主标题字号很大，横向约占画面宽度85%<br>2. 主标题字号大，横向约占画面宽度70%，周围留白更多 |
| 副标题处理 | 1. 副标题为倾斜的超粗字，填充点缀色，带黑色粗描边，像一枚贴纸，压在主标题下方<br>2. 副标题写在一张斜贴的小白便签上，上方用一段半透明胶带固定<br>3. 副标题写在一枚焦糖棕色胶囊形贴纸上，旁边有几道手绘放射短线 |
| 产品位置 | 1. 产品居中<br>2. 产品略偏右<br>3. 产品略偏左<br>4. 产品居中偏下，底部略微出画 |
| 产品大小 | 1. 产品约占画面高度55%<br>2. 产品约占画面高度65%<br>3. 产品约占画面高度75%，上端略压住标题色块 |
| 产品固定方式 | 1. 产品顶部用一枚黑色图钉固定<br>2. 产品四角各贴一小段半透明胶带<br>3. 产品一角用一枚银色回形针夹住<br>4. 产品直接压在纸上，只有柔和投影 |
| 卖点排布 | 1. 卖点混搭排布：第一个卖点写在奶黄色圆形色块里，外面套一个细黑方框，用手绘黑色弧形箭头指向产品；其余卖点写在斜贴的灰色撕边纸胶带上，散落在产品两侧<br>2. 每个卖点写在一条斜贴的半透明灰色纸胶带上，散落在产品两侧<br>3. 每个卖点写在一张小便签纸上，用胶带或回形针固定在产品周围<br>4. 卖点竖排成清单，写在一张撕边白纸上，每行前有一个手绘勾，纸片贴在产品旁<br>5. 每个卖点写在一块斜贴的奶黄色长方形标签上，散落在产品两侧 |
| 点缀色 | 1. 荧光黄绿<br>2. 焦糖棕<br>3. 不加点缀色，只用奶黄 |
| 点缀 | 1. 几道手绘放射短线和一个手绘星星<br>2. 一枚黑色图钉和一枚银色回形针<br>3. 一条手绘弧形箭头和几个小圆点<br>4. 无额外点缀，保持干净 |

冲突（不同时出现）：副标题处理1 + 点缀色3；卖点排布4 + 产品大小3；标题处理3 + 标题大小1

## ④ 文字约束

```
画面中只允许出现以下文字：主标题、副标题和卖点，每段文字只出现一次，字形清晰、完全准确，其中的英文、数字和型号按原样逐字写出。不要把卖点拆开、拼接或重新组合成新的文字。所有纸张、纸条、胶带、便签、贴纸上除指定文字外均为空白，不要出现报纸印刷字、杂志内文、英文小字、手写潦草字、页码、数字、型号、logo或任何伪文字。
```

## ⑤ 反向提示词

```
乱码, 伪文字, 报纸文字, 杂志内文, 印刷小字, 英文小字, 潦草手写字, 多余文字, 重复文字, 错别字, 模糊文字, 页码, 水印, logo, 产品变形, 透视歪斜, 卡通人物, 人物, 过度饱和, 霓虹色, 3D渲染, 杂乱堆砌, 低分辨率
```

## 样图

测试文字，链接可能过期；完整 prompt 和 seed 见 [`samples.json`](samples.json)。更多对比见 [tests/difficulty](../../tests/difficulty/README.md)。

[s2v2-1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/28/20261104/ed759433/b9e3598a-c419-4490-ac71-15467af13254_qwen_image3_serving_output_0.png?Expires=1793881355&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=%2FoO9S0FgOrp%2BDkqts4djtwuOjVc%3D) · [s2v2-2](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/20/20261104/ed759433/db097ceb-5b0e-4b0f-867d-88a6229380b0_qwen_image3_serving_output_0.png?Expires=1793881390&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=lO%2FCBM6x7Yeo2WLv4VIin0BaWlo%3D) · [s2v2-3](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/5c/20261104/ed759433/0e01e81e-6b33-4dd8-b6cd-a8ddf853fb49_qwen_image3_serving_output_0.png?Expires=1793881390&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=XoiFarQ6ZpTFl2yEqhasxWwcl1s%3D) · [s2v2-4](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/3f/20261104/ed759433/cb2b6b62-4c0d-4cb0-810c-fb8053fa2d42_qwen_image3_serving_output_0.png?Expires=1793881390&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=CpnSE9L2%2FdiefiiPf%2FjHxNiRraY%3D) · [s2v2-5](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/a0/20261104/ed759433/f4755e57-5b4b-4530-ae8f-b5cec19aac0c_qwen_image3_serving_output_0.png?Expires=1793881415&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=2qukrI3iSulEkqAR%2FFPFG%2F8pUP8%3D) · [s2v2-6](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/0f/20261104/ed759433/e4703fc3-7e63-4d6d-89a8-d584e4b3596b_qwen_image3_serving_output_0.png?Expires=1793881416&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=gVPf3zk33X%2FX17pDo%2BrKuxyayAo%3D)
