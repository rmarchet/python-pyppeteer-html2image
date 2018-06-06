#!/usr/bin/env python3
import asyncio
from pyppeteer import launch
import sys
import os


if len(sys.argv) != 3:
    print('Usage: ./convert.py <input.html> <output.xyz>')
    sys.exit(0)

_HTML = os.path.dirname(os.path.realpath(__file__)) + "/" + sys.argv[1]
_OUTFILE = sys.argv[2]
sourcepath = 'file://' + _HTML


async def generate_pdf():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(sourcepath, {'waitUntil': 'networkidle2'})
    await page.pdf({
      'path': _OUTFILE,
      'format': 'A3',
      'printBackground': True,
      'margin': {
        'top': 0,
        'bottom': 0,
        'left': 0,
        'right': 0
      }
    })
    await browser.close()


async def generate_png():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(sourcepath)
    await page.screenshot({'path': _OUTFILE, 'fullPage': True})
    await browser.close()


if ".pdf" in _OUTFILE:
    asyncio.get_event_loop().run_until_complete(generate_pdf())
elif ".png" in _OUTFILE or ".jpg" in _OUTFILE:
    asyncio.get_event_loop().run_until_complete(generate_png())
