def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('A')
print('\N{LATIN CAPITAL LETTER A}')

#python3中的字符串是Unicode字符串而不是字节数组
#lookup()-----接受不区分大小写的标准名称，返回一个Unicode字符
#name()-----接受一个Unicode字符，返回大写形式的名称
#通过\N{name} 来引用某一字符，name为该字符的标准名称
