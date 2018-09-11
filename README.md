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
## 效果如下
![](6666.gif)
