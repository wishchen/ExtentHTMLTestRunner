# ExtentHTMLTestRunner
python使用extent report模板执行测试、生成报告

## Use
基于HTMLTestRuner改造，使用了Extent report的页面模板内容，使用方式和使用HTMLTestRuner方式一致。

```
from ExtentHTMLTestRunner import HTMLTestRunner


filename="/*/result.html"
fp=open(filename,'wb')

runner=HTMLTestRunner(
                      stream=fp,
                      title='自动化测试报告',
                      description='用例执行情况：')
```
在报告中展示截图：
- 截图须和html报告在同一目录下;
- 需要在对应的case中打印一下截图名称，截图名称以 screenshot_*.png 格式命名.
- 报告需要的extent.js、extent.css可能下载不了，如果报告展示有问题可能是这些资源没有拿到，注意检查下。


![](https://user-images.githubusercontent.com/21254276/50420065-354ad700-086f-11e9-8437-61cec335986d.gif)
报告中截图点击小图展示大图还需[优化](https://github.com/wishchen/ExtentHTMLTestRunner/issues/2)
![](https://github.com/wishchen/ExtentHTMLTestRunner/blob/master/6666.gif)
