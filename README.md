# cvereport
CVE report can generate a vulnerability briefing based on product information, giving administrators a quick overview of the latest vulnerability information for the products they manage.

Usage:
pip install requirements
python cvereport.py

Customised product information:
1. Visit https://www.cvedetails.com/
2. Search for the name of the product you need to brief
3. Find the "vendor_id" and "product_id" of the product in the hyperlinks in the search results and note them down.
  
  For example: "www.cvedetails.com ' vendor_id-33 ' product_id-13878 ' Linux-Util-linux"
  
  vendor_id=33
  
  product_id=13878
  
4. Open the "id.yma:l file, add the product name, and add the vid and pid.
  
  For example:
  
  Linux-Util:
    
    vid: 33
    
    pid: 13878
