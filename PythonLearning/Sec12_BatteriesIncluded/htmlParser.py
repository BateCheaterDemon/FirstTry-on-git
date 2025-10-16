from html.parser import HTMLParser
from urllib import request
import gzip
import re
from io import BytesIO

class PythonEventsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.events = []
        self.current_event = {}
        self.in_event = False
        self.in_title = False
        self.in_time = False
        self.in_location = False
        self.current_data = ""
        self.capture_data = False
    
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # 检查事件列表项 - 更通用的选择器
        if tag == 'li':
            classes = attrs_dict.get('class', '').split()
            if any('event' in cls.lower() for cls in classes):
                self.in_event = True
                self.current_event = {}
        
        # 检查事件标题
        elif self.in_event and tag == 'h3':
            self.in_title = True
            self.capture_data = True
        
        # 检查时间信息
        elif self.in_event and tag == 'time':
            self.in_time = True
            self.capture_data = True
            if 'datetime' in attrs_dict:
                self.current_event['datetime'] = attrs_dict['datetime']
        
        # 检查地点信息
        elif self.in_event and tag == 'span':
            classes = attrs_dict.get('class', '').split()
            if any('location' in cls.lower() for cls in classes):
                self.in_location = True
                self.capture_data = True
    
    def handle_endtag(self, tag):
        if tag == 'li' and self.in_event:
            # 保存当前事件
            if self.current_event:
                self.events.append(self.current_event.copy())
            self.in_event = False
            self.current_event = {}
        
        elif tag == 'h3' and self.in_title:
            self.in_title = False
            if self.current_data.strip():
                self.current_event['title'] = self.current_data.strip()
            self.current_data = ""
            self.capture_data = False
        
        elif tag == 'time' and self.in_time:
            self.in_time = False
            if self.current_data.strip():
                self.current_event['time'] = self.current_data.strip()
            self.current_data = ""
            self.capture_data = False
        
        elif tag == 'span' and self.in_location:
            self.in_location = False
            if self.current_data.strip():
                self.current_event['location'] = self.current_data.strip()
            self.current_data = ""
            self.capture_data = False
    
    def handle_data(self, data):
        if self.capture_data:
            self.current_data += data

def get_web_content(url):
    """获取网页内容，处理gzip压缩"""
    try:
        # 创建请求，添加headers
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        req.add_header('Accept-Encoding', 'gzip')
        
        with request.urlopen(req, timeout=10) as response:
            content_encoding = response.headers.get('Content-Encoding', '').lower()
            html_data = response.read()
            
            # 处理gzip压缩
            if 'gzip' in content_encoding:
                bio = BytesIO(html_data)
                with gzip.GzipFile(fileobj=bio) as f:
                    html_content = f.read().decode('utf-8')
            else:
                html_content = html_data.decode('utf-8')
            
            return html_content
    
    except Exception as e:
        print(f"获取网页内容时出错: {e}")
        return None

def get_python_events():
    """获取Python官网事件信息"""
    url = 'https://www.python.org/events/python-events/'
    
    html_content = get_web_content(url)
    if not html_content:
        return []
    
    # 解析HTML
    parser = PythonEventsParser()
    parser.feed(html_content)
    
    return parser.events

# 更简单的解析方法，使用正则表达式
def parse_events_with_regex(html_content):
    """使用正则表达式解析事件信息"""
    events = []
    
    # 更灵活的事件块匹配
    event_pattern = r'<li[^>]*class="[^"]*event[^"]*"[^>]*>(.*?)</li>'
    events_blocks = re.findall(event_pattern, html_content, re.DOTALL | re.IGNORECASE)
    
    for block in events_blocks:
        event = {}
        
        # 提取标题
        title_match = re.search(r'<h3[^>]*>(.*?)</h3>', block, re.DOTALL | re.IGNORECASE)
        if title_match:
            title_text = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
            if title_text:
                event['title'] = title_text
        
        # 提取时间
        time_match = re.search(r'<time[^>]*datetime="([^"]*)"[^>]*>(.*?)</time>', block, re.DOTALL | re.IGNORECASE)
        if time_match:
            event['datetime'] = time_match.group(1)
            time_text = re.sub(r'<[^>]+>', '', time_match.group(2)).strip()
            if time_text:
                event['time'] = time_text
        
        # 提取地点
        location_match = re.search(r'<span[^>]*class="[^"]*location[^"]*"[^>]*>(.*?)</span>', block, re.DOTALL | re.IGNORECASE)
        if location_match:
            location_text = re.sub(r'<[^>]+>', '', location_match.group(1)).strip()
            if location_text:
                event['location'] = location_text
        
        if event:
            events.append(event)
    
    return events

# 主程序
if __name__ == "__main__":
    print("正在获取Python官网会议信息...")
    print("=" * 60)
    
    # 获取网页内容
    url = 'https://www.python.org/events/python-events/'
    html_content = get_web_content(url)
    
    if not html_content:
        print("无法获取网页内容")
        exit(1)
    
    # 方法1: 使用HTMLParser
    print("方法1: 使用HTMLParser解析")
    events = get_python_events()
    
    if events:
        print(f"找到 {len(events)} 个Python会议:")
        print("=" * 60)
        
        for i, event in enumerate(events, 1):
            print(f"会议 {i}:")
            print(f"  名称: {event.get('title', 'N/A')}")
            print(f"  时间: {event.get('time', 'N/A')}")
            print(f"  地点: {event.get('location', 'N/A')}")
            if 'datetime' in event:
                print(f"  完整时间: {event.get('datetime', 'N/A')}")
            print("-" * 40)
    else:
        print("使用HTMLParser未找到会议信息")
    
    print("\n" + "=" * 60)
    
    # 方法2: 使用正则表达式
    print("方法2: 使用正则表达式解析")
    events_regex = parse_events_with_regex(html_content)
    
    if events_regex:
        print(f"找到 {len(events_regex)} 个Python会议:")
        print("=" * 60)
        
        for i, event in enumerate(events_regex, 1):
            print(f"会议 {i}:")
            print(f"  名称: {event.get('title', 'N/A')}")
            print(f"  时间: {event.get('time', 'N/A')}")
            print(f"  地点: {event.get('location', 'N/A')}")
            print("-" * 40)
    else:
        print("使用正则表达式也未找到会议信息")
        print("\n网页结构可能已改变，建议手动检查网站HTML结构")