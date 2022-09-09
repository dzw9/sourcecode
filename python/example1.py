from pyquery import PyQuery as pq
html='''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active">third item</li>
        <li class="item-0"><a href="link0.html">forth item</a></li>
    </ul>
</div>
'''
doc=pq(html)
li=doc('.item-0.active')
li.attr('name','wenyu')
print(li)
print(li.text())
print(li.html())
