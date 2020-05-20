

#### 一、练习题

---

##### 选择题

---

**1.[多选]：对于PO模式理解正确的是：**

- [ ] A.PO模式是基于面向对象的思想，将操作每个页面当成对象，web自动化使用PO模式来编写脚本是为了减少自动化脚本对元素定位的依赖，提高测试用例的可读性、可维护性；
- [ ] B.PO模式是对面向对象多态、继承、封装特性的应用，是自动化测试项目的最佳实践之一；
- [ ] C.只要做web自动化测试就必须得引入PO模式；
- [ ] D.使用PO模式的方式来进行web自动化测试设计所有元素定位信息在整个测试项目中都只会存在一份；

**2.[多选]：对于PO模式分层思想说法正确的是：**

- [ ] A.PO模式将每个页面当成对象分成三层进行管理:对象库层、操作层、业务层，各层分别负责不同的、唯一的工作，通过这种形式来降低代码之间的耦合性；
- [ ] B.PO对象库层专门负责管理元素定位方式和信息以及获取到测试过程中所要操作的元素对象；
- [ ] C.PO操作层专门负责管理所有元素对象操作方法，而元素对象可直接从对象库中获取；
- [ ] D.PO业务层专门组织多个元素对象的操作，独立的操作连贯起来后就是一条业务操作流程，形成业务动作，对应测试用例需要执行某测试用例的时候只需调用对应的业务层组织好的业务动作方法即可；

**3.[多选]：找出下面某对象库封装代码错误说明正确的选项：**

```python
class HomePage:
    def __int__(self):
        self.driver = DriverUtil.get_driver()#该出为获取浏览器驱动对象
    	self.input_box_1 = (By.ID,"box_1")
        self.input_box_1 = (By.ID,"box_2")
        self.click_btn = (By.ID,"btn")
   	def find_input_box_1(self):
        self.driver.find_element(*self.input_box_1)
    def find_input_box_2(self):
        self.driver.find_element(*self.input_box_1)
    	def find_click_btn(self):
        	self.driver.find_elements(*self.click_btn)
```

- [ ] A.对象库需要找回元素对象供操作层使用，上面查找元素对象的方法都没有将元素对象返回；
- [ ] B.初始化类成员变量同名；
- [ ] C.初始化方法写错成了int；
- [ ] D.find_click_btn元素方法对齐方式错误；

**4.[多选]：找出下面某操作层封装代码错误说明正确的选项：**

```python
class HomeHandler:
    def __init__(self):
        self.home_page = HomePage

   	def input_box_1(self,text):
        self.home_page.find_input_box_1().send_keys(text)
        
    def input_box_2(self,text):
        self.home_page.input_box_2.send_keys(text)
    
    def click_btn(self):
        self.driver.find_click_btn().click()
```

- [ ] A.实例化对象库层时HomePage遗漏括号；
- [ ] B.input_box_2方法中实现输入操作，调用对象库层次获取元素对象方法错误调用成了对象库层属性；
- [ ] C.input_box_1和input_box_2参数一样；
- [ ] D.3个操作方法都没有return返回；

**5.[多选]：找出下面某业务层封装代码错误说明正确的选项：**

```python
class HomeProxy:
     def __init__(self):
        self.home_handler = HomePage()
     def test_demo()
    	self.home_handler.input_box_1()
        self.home_handler.input_box_1()
        self.home_handler.click_btn
```

- [ ] A.实例化操作层错误实例化成了对象库层；
- [ ] B.调用操作层方法input_box_1、input_box_1参数遗漏，test_demo也需要从外部接受参数传递；
- [ ] C.click_btn方法丢失括号；
- [ ] D.test_demo后遗漏":"；

#### 二、提高题

##### 代码题

---

**1.使用PO模式封装TPSHOP后台管理系统登录测试用例；**

```python
"""
1、新建工程
2、创建python_package包
3、在工程根目录创建工具类py文件，编写工具类
4、新建python_package包page页面文件(PO)
5、创建case的python_package包
6、在case目录下新建testCase：编写测试用例文件
"""
```







**选做题**

---

**1、新增地址，改PO**





**2、新增商品，改PO**