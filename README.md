# Fake Online Store API

This is a flask api with limited function for getting filtered data on a variety of products. The dataset was self made and writted out by hand, for the most part, and is limited to a .json file. I am not using any databases for this api as I do not feel it is necessary for this small project. This is part of a larger project "FakeOnlineStore" that I hope to start on soon.

  Currently, I do not wish to provide access to this api for anyone and it is definitely not fit for commercial use in any form. But, if you are interested in using this api in your project, you are free to clone this repo, host it yourself and freely make any changes to it as you see fit.

  For now, I wish to move my attention away to learning new things and will be updating the data.json file semi-frquently but not to the extent that I have been earlier. This is not finished as I am not satisfied with the amount of products I have now and I will continue to work on that, but I believe that my main.py file is pretty satisfactory and I have little to change and so it's unlikely to be changed much in the future.

<br />

Product format:

  ```csharp
  {
    "description": string,
    "id": int,
    "image_by": {
      "name": "link"
    }
    "images": ["array of links"],
    "keywords": ["array of keywords"],
    "price": int,
    "ratings": int,
    "stock": int,
    "type": ["array of types"]
  }
  ```
<br />

Example Product:

  ```json
  {
    "description": "Fujifilm X-T10 camera",
    "id": 1,
    "image_by": {
      "Math": "https://unsplash.com/@builtbymath?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
    },
    "images": [
      "https://i.postimg.cc/YCp7G2Ld/math-In-K0-X-GDjr-Q-unsplash.jpg",
      "https://i.postimg.cc/8PdDzfcF/math-3-Qb-OHeq-Zn-E4-unsplash.jpg",
      "https://i.postimg.cc/vZ3sWRWb/math-k-POia9-E2d-NI-unsplash.jpg",
      "https://i.postimg.cc/fbyhCHKX/math-lf-Rlv3nuf78-unsplash.jpg"
    ],
    "keywords": [
      "fujifilm",
      "x-t10",
      "camera",
      "technology",
      "tech",
      "Fujifilm X-T10 camera"
    ],
    "price": 627.71,
    "ratings": 4.5,
    "stock": 8,
    "type": [
      "Technology"
    ]
  }
  ```

<br />

## The 4 Main Pathways

- ### "/"
<br/>

  | Parameters | Explanation | _optional_ / _required_ |
  | :---: | --- | :---: |
  | `filter_type` | Filter based on the "type" of the products. eg "Technology", "Leisure", etc | _optional_ |
  | `price` | The ranking of the products based on price. Can be "ascending" or "descending". Default is none. | _optional_ |
  | `per_page` | The number of products to be retreived per request. Default value is 10. Acceptable values are between 10 and 50. | _optional_ |
  | `page` | the page number for the list of products to be retreived | _optional_ |
<br />
  
  Example result:
  ```json
  {
    "page": 1,
    "pages": 2,
    "per_page": 10,
    "products": [
      {
        "description": "White and Black Amazon Echo Dot 2 smart speaker",
        "id": 27,
        "image_by": {
          "Find Experts at Kilta.com": "https://unsplash.com/@kilta?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash",
          "Rahul Chakraborty": "https://unsplash.com/@hckmstrrahul?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
        },
        "images": [
          "https://i.postimg.cc/0ytTzYsN/rahul-chakraborty-n-Gzv-Ze1i-WOY-unsplash.jpg",
          "https://i.postimg.cc/4NGkq4PX/rahul-chakraborty-E-m-HYosg98k-unsplash.jpg",
          "https://i.postimg.cc/PqTjDXL6/find-experts-at-kilta-com-db4jr-Nv-Zh-OQ-unsplash.jpg"
        ],
        "keywords": [
          "white",
          "black",
          "amazon",
          "echo",
          "dot",
          "smart",
          "speaker",
          "technology",
          "tech",
          "White and Black Amazon Echo Dot 2 smart speaker"
        ],
        "price": 19.99,
        "ratings": 4,
        "stock": 24,
        "type": [
          "Technology"
        ]
      },
      "..."
    ],
    "total_products": 18
  }
  ```
  <br />

- ### "/search/\<query\>"
<br/>

  | `<query>` | Pass in the search term through the url path | _required_ |
  | :---: | --- | :---: |

<br />
<br />

  | Parameters | Explanation | _optionsl_ / _required_ |
  | :---: | --- | :---: |
  | `filter_type` | Filter based on the "type" of the products. eg "Technology", "Leisure", etc | _optional_ |
  | `price` | The ranking of the products based on price. Can be "ascending" or "descending". Default is "relevance". | _optional_ |
  | `per_page` | The number of products to be retreived per request. Default is 10. Acceptable values are between 10 and 50. | _optional_ |
  | `page` | the page number for the list of products to be retreived | _optional_ |
<br />

  Example Result:

  `<query>` : `apple`

  ```json
  {
    "page": 1,
    "pages": 1,
    "per_page": 10,
    "products": [
      {
        "description": "Black Apple Homepod smart speaker",
        "id": 25,
        "image_by": {
          "Howard Bouchevereau": "https://unsplash.com/@howardbouchevereau?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash",
          "Mark Tegethoff": "https://unsplash.com/@tegethoff?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash",
          "Przemyslaw Marczynski": "https://unsplash.com/@pemmax?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
        },
        "images": [
          "https://i.postimg.cc/MZNJDbMf/howard-bouchevereau-876c-F8-YBrg-unsplash.jpg",
          "https://i.postimg.cc/J0Nw0Srw/przemyslaw-marczynski-04-TYM24-Wi2c-unsplash.jpg",
          "https://i.postimg.cc/pVFR36tJ/mark-tegethoff-f4qyr3-FWB1w-unsplash.jpg"
        ],
        "keywords": [
          "black",
          "apple",
          "home",
          "pod",
          "homepod",
          "smart",
          "speaker",
          "technology",
          "tech",
          "Black Apple Homepod smart speaker"
        ],
        "price": 299.99,
        "ratings": 4.5,
        "stock": 15,
        "type": [
          "Technology"
        ]
      },
      "...",
    ],
    "total_products": 6
  }
  ```
<br />

- ### "/id/\<id\>/"
<br />

  | `<id>` | Pass in the product id through the url path | _required_ |
  | :---: | --- | :---: |
<br/>

  Example Result:

  `<id>` : `1`

  ```json
  {
    "page": 1,
    "pages": 1,
    "per_page": 1,
    "products": [
      {
        "description": "Fujifilm X-T10 camera",
        "id": 1,
        "image_by": {
          "Math": "https://unsplash.com/@builtbymath?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
        },
        "images": [
          "https://i.postimg.cc/YCp7G2Ld/math-In-K0-X-GDjr-Q-unsplash.jpg",
          "https://i.postimg.cc/8PdDzfcF/math-3-Qb-OHeq-Zn-E4-unsplash.jpg",
          "https://i.postimg.cc/vZ3sWRWb/math-k-POia9-E2d-NI-unsplash.jpg",
          "https://i.postimg.cc/fbyhCHKX/math-lf-Rlv3nuf78-unsplash.jpg"
        ],
        "keywords": [
          "fujifilm",
          "x-t10",
          "camera",
          "technology",
          "tech",
          "Fujifilm X-T10 camera"
        ],
        "price": 627.71,
        "ratings": 4.5,
        "stock": 8,
        "type": [
          "Technology"
        ]
      }
    ],
    "total_products": 1
  }
  ```
<br />

- ### "/similar/"
<br />

  | Parameters | Explanation | _optional_ / _required_ |
  | :---: | --- | :--- |
  | `id` | Uses the keywords from the product with the passed in id to search for similar products | _required_<sup id="2">[1](#1)</sup> |
  | `keywords` | Keywords can be passed in and products with these keywords are displayed | _required_<sup>[1](#1)</sup> |
  | `per_page` | The number of products to be retreived per request. Default is 5. Acceptable values are between 5 and 10. | _optional_ |

<br />

   <sup id="1">[1](#2)</sup> Only one of `id` or `keywords` should be passed in. If both is passed in, priority will be given to `id`.

<br />

  Exaple Result:

  `id` = `1`

  ```json
  {
    "page": 1,
    "pages": 1,
    "per_page": 5,
    "products": [
      {
        "description": "black Canon EOS Rebel-series DSLR camera",
        "id": 0,
        "image_by": {
          "Andrew Hutchings": "https://unsplash.com/@a_hutchings5894?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
        },
        "images": [
          "https://i.postimg.cc/k5v7Y633/andrew-hutchings-W2-Dta-Yiwfw-unsplash.jpg"
        ],
        "keywords": [
          "canon",
          "eos",
          "rebel",
          "series",
          "rebel-series",
          "dslr",
          "camera",
          "technology",
          "tech",
          "black Canon EOS Rebel-series DSLR camera"
        ],
        "price": 479.99,
        "ratings": 4.5,
        "stock": 12,
        "type": [
          "Technology"
        ]
      },
      "..."
    ],
    "total_products": 5
  }
  ```
<br />

## Image Shoutout

- Photo by <a href="https://unsplash.com/@a_hutchings5894?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Andrew Hutchings</a> on <a href="https://unsplash.com/photos/black-canon-eos-rebel-series-dslr-camera-W2Dta_Yiwfw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@neonbrand?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Kenny Eliason</a> on <a href="https://unsplash.com/photos/person-carrying-canon-dslr-camera-3ngFVZVU_LE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@builtbymath?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Math</a> on <a href="https://unsplash.com/photos/black-fujifilm-bridge-camera-InK0X-GDjrQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@goby?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Goby</a> on <a href="https://unsplash.com/photos/four-electric-toothbrushes-zHMpGLOD8nI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@lightwear?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">LightWear SkinCare</a> on <a href="https://unsplash.com/photos/gold-colore-jaw-shaper-EGGpnSmIErA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@danielkorpai?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Daniel Korpai</a> on <a href="https://unsplash.com/photos/space-gray-apple-watch-with-black-sports-band-hbTKIbuMmBI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a> <br />
- Photo by <a href="https://unsplash.com/@ikredenets?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Irene Kredenets</a> on <a href="https://unsplash.com/photos/brown-bag-on-white-wall-Jm_SqbqZYkY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@moritz_photography?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Moritz Kindler</a> on <a href="https://unsplash.com/photos/charcoal-google-home-mini-speaker-en-9cltURag?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@benceboros?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">BENCE BOROS</a> on <a href="https://unsplash.com/photos/turned-on-charcoal-google-home-mini-and-smartphone-anapPhJFRhM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@elfcodobelf?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Andreea Popa</a> on <a href="https://unsplash.com/photos/coral-google-home-mini-X8yEM2NCnCM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@benkolde?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Ben Kolde</a> on <a href="https://unsplash.com/photos/flat-lay-photography-of-coral-google-home-mini-on-black-surface-beside-apple-airpods-d6dxQwmxV2Q?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@leisara?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Leisara Studio</a> on <a href="https://unsplash.com/photos/brown-leather-handbag-beside-macbook-pro-EzzW1oNek-I?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@uyk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Haryo Setyadi</a> on <a href="https://unsplash.com/photos/white-crew-neck-t-shirt-acn5ERAeSb4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
- Photo by <a href="https://unsplash.com/@anomaly?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Anomaly</a> on <a href="https://unsplash.com/photos/man-wearing-white-crew-neck-t-shirts-WWesmHEgXDs?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@ryanhoffman007?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Ryan Hoffman</a> on <a href="https://unsplash.com/photos/black-crew-neck-t-shirt-Cs4GVbMqKGY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@karlkoehler?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Karl Köhler</a> on <a href="https://unsplash.com/photos/black-mizu-stainless-steel-tumbler-dGIEMeN2MV8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@maalcreates?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jamaal Kareem</a> on <a href="https://unsplash.com/photos/yellow-and-black-sports-bottle-YDRrskIdMDw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@joanofarts?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Joan Tran</a> on <a href="https://unsplash.com/photos/green-bottle-on-white-table-reEySFadyJQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@groblechnersara?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Sara Groblechner</a> on <a href="https://unsplash.com/photos/brown-wooden-bottle-on-white-table-h10-NImYZHs?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@mediamodifier?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mediamodifier</a> on <a href="https://unsplash.com/photos/white-baseball-cap-on-white-surface-t8HiP3e5abg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@marcmll?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Marc Mueller</a> on <a href="https://unsplash.com/photos/silver-oculus-go-headset-box-zQLV9DJYo4I?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@gieling?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Remy Gieling</a> on <a href="https://unsplash.com/photos/pink-and-white-vr-goggles-Zf0mPf4lG-U?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@alex_andrews?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Alexander Andrews</a> on <a href="https://unsplash.com/photos/black-nikon-body-camera-gZbEl9JTnGk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@kellysikkema?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Kelly Sikkema</a> on <a href="https://unsplash.com/photos/space-gray-ipad-with-apple-pencil-with-white-and-black-pinstriped-background-4xHgz_ZllQs?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@jamesyarema?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">James Yarema</a> on <a href="https://unsplash.com/photos/round-gray-ball-on-brown-wooden-table-sz6W3auVnHQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@howardbouchevereau?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Howard Bouchevereau</a> on <a href="https://unsplash.com/photos/black-apple-homepod-speaker-on-table-876c-F8YBrg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@pemmax?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Przemyslaw Marczynski</a> on <a href="https://unsplash.com/photos/black-portable-speaker-04TYM24Wi2c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@tegethoff?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mark Tegethoff</a> on <a href="https://unsplash.com/photos/black-apple-homepod-speaker-on-table-f4qyr3FWB1w?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@nicolaslafargue?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Nicolas Lafargue</a> on <a href="https://unsplash.com/photos/tubular-white-bluetooth-speaker-on-white-surface-2FcSIYJQkTM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@theblowup?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">the blowup</a> on <a href="https://unsplash.com/photos/white-knit-crew-neck-shirt-Hh36dzgTLVY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@nadyeldems?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Dan Smedley</a> on <a href="https://unsplash.com/photos/green-plant-on-white-pot-8gN01V0nrOU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@hckmstrrahul?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Rahul Chakraborty</a> on <a href="https://unsplash.com/photos/black-amazon-echo-dot-speaker-E_mHYosg98k?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@kilta?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Find Experts at Kilta.com</a> on <a href="https://unsplash.com/photos/white-and-black-amazon-echo-dot-2-db4jrNvZhOQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@dominostudio?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Domino Studio</a> on <a href="https://unsplash.com/photos/unpaired-red-nike-sneaker-164_6wVEHfI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@cdx2?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">C D-X</a> on <a href="https://unsplash.com/photos/black-wireless-headphones-dBwadhWa-lI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@alexunderhess?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Alexunder Hess</a> on <a href="https://unsplash.com/photos/gold-beats-wireless-headphones-bWZAPKm0zZE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@komarov?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Komarov Egor 🇺🇦</a> on <a href="https://unsplash.com/photos/a-black-cell-phone-ECHU29RXMhs?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@laurachouette?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Laura Chouette</a> on <a href="https://unsplash.com/photos/black-and-silver-calvin-klein-perfume-bottle-_ODRA1MPL1I?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@glennclaire?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Glenna Haug</a> on <a href="https://unsplash.com/photos/white-and-black-usb-flash-drive-DuNXXPScbJM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><br />
- Photo by <a href="https://unsplash.com/@linaverovaya?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Lina Verovaya</a> on <a href="https://unsplash.com/photos/pink-and-white-plastic-tube-bottle-BibJjO4sYrI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>