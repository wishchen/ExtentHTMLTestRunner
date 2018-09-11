# ExtentHTMLTestRunner
Create test report with Extent report use python

## Use
基于HTMLTestRuner改造，使用了Extent report的页面模板内容，使用方式和使用HTMLTestRuner方式一致。

```
filename="/*/result.html"
fp=open(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
                                    stream=fp,
                                    title='自动化测试报告',
                                    description='用例执行情况：')
```
在报告中展示截图：需要在对应的case中打印一下截图名称，截图名称以 screenshot_*.png 格式命名
## 效果如下
![](6666.gif)
