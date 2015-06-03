#!/usr/bin/env python3

import os
import cgi
import html


def writeTag(tag, *texts):
  return '<{0}>{1}</{0}>'.format(tag, ''.join(texts))


if __name__ == '__main__':
  form = cgi.FieldStorage()
  #
  data = {}
  data['first_name'] = form.getvalue('first_name')
  data['last_name'] = form.getvalue('last_name')
  data['text_content'] = form.getvalue('text_content')
  #
  err_arr = []
  suc_arr = []
  for (field, text) in data.items():
    if not data[field]:
      err_arr.append("err_" + field + '=' + "Cannot be empty!")
    else:
      data[field] = html.unescape(text)
      suc_arr.append(field + '=' + data[field])
  #
  if not err_arr:
    print('Content-type:text/html\r\n\r\n', end = '')
    print(writeTag('html',
           writeTag('head',
             '<meta charset="utf-8">',
             writeTag('title', 'Form')
           ),
           writeTag('body',
             writeTag('h2', 'Information about {first_name} {last_name}'.format(**data)),
             writeTag('p', data['text_content'])
           )
         )
       )
  else:
    err = "&".join(err_arr + suc_arr)
    print("Location:http://{0}/index.php?{1}\n\n".format(os.environ['SERVER_ADDR'], err))
