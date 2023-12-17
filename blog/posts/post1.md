title: How to build a website
description: This is my first entry
date: 2023-12-15
permissions: PUBLIC
tags:
  - how-to
  - webdev
post_image: https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no
images:
  fireplace:
    google_url: https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no
    title: cozy fire
    description: This is a test
  fireplace1:
    google_url: https://lh3.googleusercontent.com/pw/AMWts8Bx2iWHOIhdECCtwMRD86tBZOrm0MAhnVqdX_btgQ7cB6ciu-x1YBqg-5VCSUsMa5AVhz_CoNBwcE1WPZ6H41GxQnowFJp8dZ1acQumpV2H5Rcz5imtqOdnUPKTQ1G49k4yKuFuL3arokAUJ-d_mEEmoA=w1202-h2136-no
    title: cozy fire
    description: This is a test
  fireplace2:
    google_url: https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no
    title: cozy fire
    description: This is a test
  fireplace3:
    google_url: https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no
    title: cozy fire
    description: This is a test
  fireplace4:
    google_url: https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no
    title: cozy fire
    description: This is a test
  fireplace5:
    google_url: https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no
    title: cozy fire
    description: This is a test
---





# Introduction
Stay at home parenting is fun, and time consuming, but I sometimes need some thought-provoking distractions. That distraction has mostly been in the form of woodworking and settng up a machineshop in our garage but sometimes I just want to code something. I also miss just taking notes, and writing documentation that has been a big part of my professional career. Hence, lets make a blog? I previously had a local jekyll site running with some notes and projects ideas that mostly remained private, some of which I'll move here. I wanted to make something with more functionality than the static site generator jekyll, something that would allow me to make a few interactive components too - like capturing time-series temperature data for some recipes would be fun.

{{ gallery(page.images)  | safe }}


# Useful guides and tutorials

 - The [flask project page](https://flask.palletsprojects.com/en/3.0.x/) has great descriptions and some simple examples of most components I needed for this build. 

 - The [flask-login](https://flask-login.readthedocs.io/en/latest/) which was used to handle a user state across the site.

 - The [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) which was used for handling the site database for users, comments, permisions, etc.

 - This series by [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) was especially helpful as one of the more complete getting started guides I found. It's helpful to have one person explaining things from hello-world through databases and all the way to deploying. I often get distracted by details and will spend a day looking  on something non-sensibly generic like best practices for user-schema for website (soo specifics needed to have a useful answer) before I get back to what I was doing. Miguel's tutorial lets me save that step for later and just follow his example through the end. 

 - This [flask google login](https://realpython.com/flask-google-login/) tutorial has nice examples of adding a google-sign in functionality, I later discovered flask-dance, but I ran into trouble connecting it to the standard [google-sign-in scripts](https://developers.google.com/identity/gsi/web/guides/display-button) so I switched back to the oauth library directly.


photorama galleries.
Jekyll clean Dark theme

flask blog introduction 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


https://realpython.com/flask-google-login/

https://letsencrypt.org/getting-started/

https://www.digitalocean.com/community/tutorials/how-to-use-certbot-standalone-mode-to-retrieve-let-s-encrypt-ssl-certificates-on-ubuntu-22-04



[flask jinja context processor](https://flask.palletsprojects.com/en/2.3.x/templating/)


generate local certificate
openssl req -x509 -out localhost.crt -keyout localhost.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")



trust local certificate
sudo mkdir /usr/local/share/ca-certificates/extra
sudo cp foo.crt /usr/local/share/ca-certificates/extra/foo.crt
sudo dpkg-reconfigure ca-certificates
sudo update-ca-certificates


<a class="popup" href="https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no">Open popup</a>


<!-- <figure class="gallery-item">
    <header class='gallery-icon'>
    <a class="popup img-responsive" href="https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no" title="image_caption" data-caption="image_Description">
    <img src="https://lh3.googleusercontent.com/pw/AMWts8AhcLCaaBQUVAJo-k3zM4S3NiulNspH6lIocBxF_5KIEwWKx8ETiH5_tbHRMz-ZH994WASzFvW8twUVTRhNoOhPybH8FERSJuTcAY4bRttyHdAHPNJefHTtFe0CBYRAmLdR-vsh5CfBjyOrwZd74m_aBw=w3692-h2078-no"></a>
    </header> 
    <figcaption class='gallery-caption'>
      <div class="entry-summary" id="image_caption">
          <h3>image_caption</h3>
          <p>image_description today we got blah dop ta ta</p>
      </div>
    </figcaption>
</figure> -->




    :::python
    # Testing code highlighting
    x = a + b
    print('This is a python string')
    def alpha(ball):
    return 'cat'
    def balloon(y):
    return y**2

    print('done')




{{ gallery(page.images) | safe}}




This is an equation $ \alpha=10^25 $