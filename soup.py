import requests
from bs4 import BeautifulSoup


class Soup:

    def __init__(self):
        self.soup = None
        self.html = None
        self.listings = None
        self.list = []
        self.inserat = []

    def set_soup(self, text):
        self.soup = BeautifulSoup(text, 'html.parser')

    def get_soup(self):
        return self.soup.prettify()

    def get_listing(self):
        # return self.soup.find_all("div", class_="result-list-entry__data")
        global entfernung, entfernung
        self.listings = self.soup.find_all("div", class_="result-list-entry__data")
        for listing in self.listings:  # Todo Hier in dict erst speichern dann Liste
            if listing is not None:


                name_tag = listing.find("a", class_="result-list-entry__brand-title-container")
                if name_tag is not None:
                    name_tag = name_tag.find("h2").get_text()
                    if name_tag[0:3] == "NEU":
                        name_tag = name_tag[3:-1]
                else:
                    name_tag = ""

                adresse = listing.find("button", class_="result-list-entry__map-link")#.get_text()
                content = listing.find_all("dd", class_="font-highlight")
                preis = content[0]#.get_text().strip("€").replace(',', '')) #Integer Type Casting
                flaeche = content[1]#.get_text().strip(" m²").replace(',', '')
                zimmer = listing.find("span", class_="onlyLarge")#.get_text().replace(',', '.')
                link = listing.find("a", class_="result-list-entry__brand-title-container").get("href")
                entfernung = listing.find("div", "margin-right-xs")
                # if entfernung is not None:
                #     entfernung = float(entfernung.get_text().split("km |")[0])



                daten = {
                    "name_tag": name_tag,
                    "adresse" : adresse.get_text() if adresse is not None else "",
                    "preis" : float(preis.get_text().strip("€").replace(',', '')) if preis is not None else "",
                    "flaeche" : float(flaeche.get_text().strip(" m²").replace(',', '')) if flaeche is not None else "",
                    "zimmer" : float(zimmer.get_text().replace(',', '.')) if zimmer is not None else "",
                    "link" : link if link is not None else "",
                    "entfernung" : float(entfernung.get_text().split("km |")[0]) if entfernung is not None else "",

                }

                print(daten)


            else:
                continue

    # [{}]

    def set_html(self, html):
        self.html = html

test2 = r"""<html lang="de"><head>
  
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
  <meta name="msapplication-config" content="none">
  <meta name="format-detection" content="telephone=no">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">

  
  <link rel="preconnect" href="https://static-immobilienscout24.de">
  
      <link rel="preconnect" href="https://pro-sov-agent-api.is24-realtor-directory.s24cloud.net" crossorigin="">
  

  <title>Wohnung mieten im Umkreis von 5 km von Gießen (Kreis) - ImmoScout24</title>
  
    








	
	
		<meta name="robots" content="noindex, follow">
	


<meta name="description" content="Ein großes Angebot an Mietwohnungen im Umkreis von 5 km von Gießen (Kreis) finden Sie bei ImmoScout24. Jetzt Ihre Traum-Wohnung im Umkreis von 5 km von Gießen (Kreis) mieten.">
<meta name="keywords" content="">


  

  








<link rel="preload" href="https://www.static-immobilienscout24.de/fro/core/5.3.0/font/vendor/make-it-sans/MakeItSansIS24WEB-Regular.woff2" as="font" type="font/woff2" crossorigin="">
<link rel="preload" href="https://www.static-immobilienscout24.de/fro/core/5.3.0/font/vendor/make-it-sans/MakeItSansIS24WEB-Bold.woff2" as="font" type="font/woff2" crossorigin="">
<link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/cosma-ui-icons/6.4.0/s24-icons.css">
<link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/core/5.3.0/css/core.min.css">
<link rel="stylesheet" href="/Suche/resources/build/resultlist.css?v=f8f6b5d0e9153ea1a84d">
<link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/slick/1.8.1/slick-min.css">
<link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/gac/4.0.10/gac.min.css">
<link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/bootstrap-tooltip/0.0.3/tooltip.css">

<style id="topnavigation__style-element" type="text/css" media="all">
    /*!
 * ImmobilienScout24 Top Navigation CSS, v4.9.0
 * http://www.immobilienscout24.de/
 */@-moz-keyframes dropin{0%{max-height:0}100%{max-height:100vh}}@-webkit-keyframes dropin{0%{max-height:0}100%{max-height:100vh}}@-ms-keyframes dropin{0%{max-height:0}100%{max-height:100vh}}@keyframes dropin{0%{max-height:0}100%{max-height:100vh}}@-moz-keyframes dropdown{0%{max-height:100vh}100%{max-height:0}}@-webkit-keyframes dropdown{0%{max-height:100vh}100%{max-height:0}}@-ms-keyframes dropdown{0%{max-height:100vh}100%{max-height:0}}@keyframes dropdown{0%{max-height:100vh}100%{max-height:0}}@-moz-keyframes fadeoutbackground{from{background-color:rgba(0,0,0,.5)}to{background-color:rgba(0,0,0,0)}}@-webkit-keyframes fadeoutbackground{from{background-color:rgba(0,0,0,.5)}to{background-color:rgba(0,0,0,0)}}@-ms-keyframes fadeoutbackground{from{background-color:rgba(0,0,0,.5)}to{background-color:rgba(0,0,0,0)}}@keyframes fadeoutbackground{from{background-color:rgba(0,0,0,.5)}to{background-color:rgba(0,0,0,0)}}@-moz-keyframes fadeinbackground{from{background-color:rgba(0,0,0,0)}to{background-color:rgba(0,0,0,.5)}}@-webkit-keyframes fadeinbackground{from{background-color:rgba(0,0,0,0)}to{background-color:rgba(0,0,0,.5)}}@-ms-keyframes fadeinbackground{from{background-color:rgba(0,0,0,0)}to{background-color:rgba(0,0,0,.5)}}@keyframes fadeinbackground{from{background-color:rgba(0,0,0,0)}to{background-color:rgba(0,0,0,.5)}}@-moz-keyframes fadeout{from{opacity:1}to{opacity:0}}@-webkit-keyframes fadeout{from{opacity:1}to{opacity:0}}@-ms-keyframes fadeout{from{opacity:1}to{opacity:0}}@keyframes fadeout{from{opacity:1}to{opacity:0}}@-moz-keyframes fadein{from{opacity:0}to{opacity:1}}@-webkit-keyframes fadein{from{opacity:0}to{opacity:1}}@-ms-keyframes fadein{from{opacity:0}to{opacity:1}}@keyframes fadein{from{opacity:0}to{opacity:1}}.page-header .link-container .icon,.page-header .link-container>.link,.sidebarnavigation .link-container .icon,.sidebarnavigation .link-container>.link{display:block;color:#333}.page-header .link-container>.icon,.sidebarnavigation .link-container>.icon{text-align:center}.page-header .link-container.active>.page-header__link.link,.sidebarnavigation .link-container.active>.page-header__link.link{font-weight:700;text-decoration:underline!important;text-decoration-thickness:2px!important;text-underline-offset:6px!important}.page-header .link-container:not(.active)>.link,.sidebarnavigation .link-container:not(.active)>.link{font-weight:700}.page-header .link-container:not(.active):hover,.sidebarnavigation .link-container:not(.active):hover{cursor:pointer!important}.page-header .link-container:not(.active):hover>.link,.sidebarnavigation .link-container:not(.active):hover>.link{text-decoration:underline!important;text-decoration-thickness:2px!important;text-underline-offset:6px!important}.page-header .active:hover,.sidebarnavigation .active:hover{cursor:default!important}.page-header .hide,.sidebarnavigation .hide{display:none}@media (max-width:668px){.page-header .palm-hide,.sidebarnavigation .palm-hide{display:none}}.page-header .line-height-0,.sidebarnavigation .line-height-0{line-height:0!important}.page-header .line-height-xs,.sidebarnavigation .line-height-xs{line-height:4px!important}.page-header .line-height-s,.sidebarnavigation .line-height-s{line-height:8px!important}.page-header .line-height-m,.sidebarnavigation .line-height-m{line-height:16px!important}.page-header .line-height-l,.sidebarnavigation .line-height-l{line-height:24px!important}.page-header .line-height-xl,.sidebarnavigation .line-height-xl{line-height:32px!important}.page-header .line-height-xxl,.sidebarnavigation .line-height-xxl{line-height:40px!important}.page-header .line-height-xxxl,.sidebarnavigation .line-height-xxxl{line-height:48px!important}.page-header .line-height-17,.sidebarnavigation .line-height-17{line-height:17px!important}.page-header .line-height-22,.sidebarnavigation .line-height-22{line-height:22px!important}.page-header .line-height-29,.sidebarnavigation .line-height-29{line-height:29px!important}.page-header .font-size-l,.sidebarnavigation .font-size-l{font-size:24px!important}.page-header .font-size-12,.sidebarnavigation .font-size-12{font-size:12px!important}.page-header .font-size-14,.sidebarnavigation .font-size-14{font-size:14px!important}.page-header .font-size-18,.sidebarnavigation .font-size-18{font-size:18px!important}.page-header .font-size-20,.sidebarnavigation .font-size-20{font-size:20px!important}.page-header .height-xs,.sidebarnavigation .height-xs{height:4px!important}.page-header .height-s,.sidebarnavigation .height-s{height:8px!important}.page-header .height-m,.sidebarnavigation .height-m{height:16px!important}.page-header .height-l,.sidebarnavigation .height-l{height:24px!important}.page-header .height-xl,.sidebarnavigation .height-xl{height:32px!important}.page-header .height-xxl,.sidebarnavigation .height-xxl{height:40px!important}.page-header .height-xxxl,.sidebarnavigation .height-xxxl{height:48px!important}.page-header .width-xs,.sidebarnavigation .width-xs{width:4px!important}.page-header .width-s,.sidebarnavigation .width-s{width:8px!important}.page-header .width-m,.sidebarnavigation .width-m{width:16px!important}.page-header .width-l,.sidebarnavigation .width-l{width:24px!important}.page-header .width-xl,.sidebarnavigation .width-xl{width:32px!important}.page-header .width-xxl,.sidebarnavigation .width-xxl{width:40px!important}.page-header .width-xxxl,.sidebarnavigation .width-xxxl{width:48px!important}.page-header .margin-vertical-auto,.sidebarnavigation .margin-vertical-auto{margin-top:auto;margin-bottom:auto}.page-header .margin-left-auto,.sidebarnavigation .margin-left-auto{margin-left:auto!important}.page-header .margin-right-auto,.sidebarnavigation .margin-right-auto{margin-right:auto!important}@media (min-width:1014px){.page-header .desk-line-height-xs,.sidebarnavigation .desk-line-height-xs{line-height:4px!important}.page-header .desk-line-height-s,.sidebarnavigation .desk-line-height-s{line-height:8px!important}.page-header .desk-line-height-m,.sidebarnavigation .desk-line-height-m{line-height:16px!important}.page-header .desk-line-height-l,.sidebarnavigation .desk-line-height-l{line-height:24px!important}.page-header .desk-line-height-xl,.sidebarnavigation .desk-line-height-xl{line-height:32px!important}.page-header .desk-line-height-xxl,.sidebarnavigation .desk-line-height-xxl{line-height:40px!important}.page-header .desk-line-height-xxxl,.sidebarnavigation .desk-line-height-xxxl{line-height:48px!important}.page-header .desk-line-height-18,.sidebarnavigation .desk-line-height-18{line-height:18px!important}.page-header .desk-height-28,.sidebarnavigation .desk-height-28{height:28px!important}.page-header .desk-height-36,.sidebarnavigation .desk-height-36{height:36px!important}.page-header .desk-height-xs,.sidebarnavigation .desk-height-xs{height:4px!important}.page-header .desk-height-s,.sidebarnavigation .desk-height-s{height:8px!important}.page-header .desk-height-m,.sidebarnavigation .desk-height-m{height:16px!important}.page-header .desk-height-l,.sidebarnavigation .desk-height-l{height:24px!important}.page-header .desk-height-xl,.sidebarnavigation .desk-height-xl{height:32px!important}.page-header .desk-height-xxl,.sidebarnavigation .desk-height-xxl{height:40px!important}.page-header .desk-height-xxxl,.sidebarnavigation .desk-height-xxxl{height:48px!important}.page-header .desk-width-36,.sidebarnavigation .desk-width-36{width:36px!important}.page-header .desk-width-xs,.sidebarnavigation .desk-width-xs{width:4px!important}.page-header .desk-width-s,.sidebarnavigation .desk-width-s{width:8px!important}.page-header .desk-width-m,.sidebarnavigation .desk-width-m{width:16px!important}.page-header .desk-width-l,.sidebarnavigation .desk-width-l{width:24px!important}.page-header .desk-width-xl,.sidebarnavigation .desk-width-xl{width:32px!important}.page-header .desk-width-xxl,.sidebarnavigation .desk-width-xxl{width:40px!important}.page-header .desk-width-xxxl,.sidebarnavigation .desk-width-xxxl{width:48px!important}}@media (min-width:669px) and (max-width:1013px){.page-header .lap-line-height-0,.sidebarnavigation .lap-line-height-0{line-height:0!important}.page-header .lap-line-height-xs,.sidebarnavigation .lap-line-height-xs{line-height:4px!important}.page-header .lap-line-height-s,.sidebarnavigation .lap-line-height-s{line-height:8px!important}.page-header .lap-line-height-m,.sidebarnavigation .lap-line-height-m{line-height:16px!important}.page-header .lap-line-height-l,.sidebarnavigation .lap-line-height-l{line-height:24px!important}.page-header .lap-line-height-xxl,.sidebarnavigation .lap-line-height-xxl{line-height:40px!important}.page-header .lap-line-height-xl,.sidebarnavigation .lap-line-height-xl{line-height:32px!important}.page-header .lap-line-height-xxxl,.sidebarnavigation .lap-line-height-xxxl{line-height:48px!important}.page-header .lap-height-28,.sidebarnavigation .lap-height-28{height:28px!important}.page-header .lap-height-36,.sidebarnavigation .lap-height-36{height:36px!important}.page-header .lap-height-xs,.sidebarnavigation .lap-height-xs{height:4px!important}.page-header .lap-height-s,.sidebarnavigation .lap-height-s{height:8px!important}.page-header .lap-height-m,.sidebarnavigation .lap-height-m{height:16px!important}.page-header .lap-height-l,.sidebarnavigation .lap-height-l{height:24px!important}.page-header .lap-height-xl,.sidebarnavigation .lap-height-xl{height:32px!important}.page-header .lap-height-xxl,.sidebarnavigation .lap-height-xxl{height:40px!important}.page-header .lap-height-xxxl,.sidebarnavigation .lap-height-xxxl{height:48px!important}.page-header .lap-width-36,.sidebarnavigation .lap-width-36{width:36px!important}.page-header .lap-width-xs,.sidebarnavigation .lap-width-xs{width:4px!important}.page-header .lap-width-s,.sidebarnavigation .lap-width-s{width:8px!important}.page-header .lap-width-m,.sidebarnavigation .lap-width-m{width:16px!important}.page-header .lap-width-l,.sidebarnavigation .lap-width-l{width:24px!important}.page-header .lap-width-xl,.sidebarnavigation .lap-width-xl{width:32px!important}.page-header .lap-width-xxl,.sidebarnavigation .lap-width-xxl{width:40px!important}.page-header .lap-width-xxxl,.sidebarnavigation .lap-width-xxxl{width:48px!important}}@media (max-width:668px){.page-header .palm-line-height-0,.sidebarnavigation .palm-line-height-0{line-height:0!important}.page-header .palm-line-height-xs,.sidebarnavigation .palm-line-height-xs{line-height:4px!important}.page-header .palm-line-height-s,.sidebarnavigation .palm-line-height-s{line-height:8px!important}.page-header .palm-line-height-m,.sidebarnavigation .palm-line-height-m{line-height:16px!important}.page-header .palm-line-height-l,.sidebarnavigation .palm-line-height-l{line-height:24px!important}.page-header .palm-line-height-xl,.sidebarnavigation .palm-line-height-xl{line-height:32px!important}.page-header .palm-line-height-xxl,.sidebarnavigation .palm-line-height-xxl{line-height:40px!important}.page-header .palm-line-height-xxxl,.sidebarnavigation .palm-line-height-xxxl{line-height:48px!important}.page-header .palm-height-28,.sidebarnavigation .palm-height-28{height:28px!important}.page-header .palm-height-xs,.sidebarnavigation .palm-height-xs{height:4px!important}.page-header .palm-height-s,.sidebarnavigation .palm-height-s{height:8px!important}.page-header .palm-height-m,.sidebarnavigation .palm-height-m{height:16px!important}.page-header .palm-height-l,.sidebarnavigation .palm-height-l{height:24px!important}.page-header .palm-height-xl,.sidebarnavigation .palm-height-xl{height:32px!important}.page-header .palm-height-xxl,.sidebarnavigation .palm-height-xxl{height:40px!important}.page-header .palm-height-xxxl,.sidebarnavigation .palm-height-xxxl{height:48px!important}.page-header .palm-width-28,.sidebarnavigation .palm-width-28{width:28px!important}.page-header .palm-width-xs,.sidebarnavigation .palm-width-xs{width:4px!important}.page-header .palm-width-s,.sidebarnavigation .palm-width-s{width:8px!important}.page-header .palm-width-m,.sidebarnavigation .palm-width-m{width:16px!important}.page-header .palm-width-l,.sidebarnavigation .palm-width-l{width:24px!important}.page-header .palm-width-xl,.sidebarnavigation .palm-width-xl{width:32px!important}.page-header .palm-width-xxl,.sidebarnavigation .palm-width-xxl{width:40px!important}.page-header .palm-width-xxxl,.sidebarnavigation .palm-width-xxxl{width:48px!important}}@media (min-width:1014px){.header-desk-padding-s{padding:8px!important}.header-desk-padding-top-xs{padding-top:4px!important}.header-desk-padding-top-s{padding-top:8px!important}.header-desk-padding-right-xs{padding-right:4px!important}.header-desk-padding-right-s{padding-right:8px!important}.header-desk-padding-horizontal-l{padding-right:24px!important;padding-left:24px!important}.header-desk-padding-vertical-s{padding-top:8px!important;padding-bottom:8px!important}.header-desk-padding-vertical-m{padding-top:16px!important;padding-bottom:16px!important}.header-desk-padding-right-l{padding-right:24px!important}.header-desk-margin-right-xxl{margin-right:40px!important}}@media (min-width:669px) and (max-width:1013px){.header-lap-padding-l{padding:24px!important}.header-lap-padding-vertical-l{padding-top:24px!important;padding-bottom:24px!important}.header-lap-padding-top-xs{padding-top:4px!important}.header-lap-padding-right-l{padding-right:24px!important}.header-lap-padding-left-l{padding-left:24px!important}.header-lap-margin-right-xl{margin-right:32px!important}}@media (max-width:668px){.header-palm-padding-l{padding:16px!important}.header-palm-padding-vertical-l{padding-top:16px!important;padding-bottom:16px!important}.header-palm-padding-top-xs{padding-top:2px!important}.header-palm-padding-right-l{padding-right:16px!important}.header-palm-padding-left-l{padding-left:16px!important}.header-palm-margin-right-xl{margin-right:24px!important}}body{-webkit-text-size-adjust:100%}.page-header{white-space:normal;-webkit-appearance:none;-webkit-font-smoothing:antialiased}.page-header,[data-theme=core] .page-header{font-family:"Make It Sans IS24 Web",Verdana,"DejaVu Sans",Arial,Helvetica,sans-serif}[data-theme=cosma] .page-header{font-family:"Make It Sans IS24 Web",Verdana,"DejaVu Sans",Arial,Helvetica,sans-serif}.header__divider{left:0;box-shadow:inset 0 -1px 0 #e0e0e0}.page-header .link-container .page-header__link{padding-bottom:2px}.page-header .link-container .page-header__login-link.link{border-bottom:2px #fff solid}.page-header .link-container.active .page-header__link.link{text-underline-offset:12px!important}.page-header .link-container.active .page-header__login-link.link{border-bottom:2px #000 solid}.page-header .link-container:not(.active):hover .page-header__link.link{text-underline-offset:12px!important}.page-header .link-container:not(.active):hover .page-header__login-link.link{border-bottom:2px #000 solid}.page-header .page-header__hamburger-container{cursor:pointer}.page-header .page-header__logo>img{width:117px}@media (min-width:1314px){.page-header__hamburger-wrapper{margin-left:-72px}}@media (min-width:669px){.page-header .page-header__hamburger-container .page-header__hamburger-button{box-sizing:content-box}.page-header .page-header__hamburger-container .page-header__hamburger-button:hover{background:#f5f5f5;border-radius:8px}.page-header .topnavigation__sso-login a:hover{text-decoration:none}.page-header .page-header__logo>img{width:137px}page-wrapper:not(.page-wrapper--full-width) .page-header{position:relative}}@media (max-width:1013px){.header__divider{margin-top:-1px;height:1px}}@media (min-width:669px){.topnavigation{flex-grow:0!important;font-size:14px;font-size:1.4rem;background-color:#fff}.topnavigation .topnavigation__slide--back{display:none}.topnavigation__hover-tabs:not(.sso-login)>li .topnavigation__hover-tabs__label:after{padding-left:4px;font-family:FontAwesome;content:"\f107"}.topnavigation__hover-tabs::after{display:table;clear:both;content:""}.topnavigation__hover-tabs>li{float:left}.topnavigation__hover-tabs>li .topnavigation__hover-tabs__label{cursor:default}.topnavigation__icon{display:none}.topnavigation__hover-tabs__label{display:block;padding-top:24px;padding-bottom:22px;line-height:1;font-size:14px;font-size:1.4rem;font-weight:600;-webkit-transition:color .15s ease;-moz-transition:color .15s ease;-o-transition:color .15s ease;transition:color .15s ease}.topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__hover-tabs__label{padding-left:20px}[data-theme=cosma] .topnavigation__hover-tabs__label{padding-left:0}.topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__hover-tabs__label{margin-left:0}[data-theme=cosma] .topnavigation__hover-tabs__label{margin-left:9px}.topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__hover-tabs__label{padding-right:20px}[data-theme=cosma] .topnavigation__hover-tabs__label{padding-right:0}.topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__hover-tabs__label{border-bottom:3px solid transparent}[data-theme=cosma] .topnavigation__hover-tabs__label{border-bottom:2px solid transparent}.topnavigation__hover-tabs__label,.topnavigation__hover-tabs__label:link,.topnavigation__hover-tabs__label:visited{text-decoration:none}.topnavigation__hover-tabs__label,.topnavigation__hover-tabs__label:link,.topnavigation__hover-tabs__label:visited,[data-theme=core] .topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__hover-tabs__label:link,[data-theme=core] .topnavigation__hover-tabs__label:visited{color:#333}[data-theme=cosma] .topnavigation__hover-tabs__label,[data-theme=cosma] .topnavigation__hover-tabs__label:link,[data-theme=cosma] .topnavigation__hover-tabs__label:visited{color:#606060}.topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg-core,[data-theme=core] .topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg-core{display:block}[data-theme=cosma] .topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg-core{display:none}.topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg-cosma,[data-theme=core] .topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg-cosma{display:none}[data-theme=cosma] .topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg-cosma{display:block}.topnavigation__overlay--account--show .topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label{color:#ff7500}[data-theme=cosma] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label{color:#333}.topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__chevronAppend--desktop,[data-theme=core] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__chevronAppend--desktop{color:inherit}[data-theme=cosma] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__chevronAppend--desktop{color:#333}.topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg #Main-Mobile-Nav,[data-theme=core] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg #Main-Mobile-Nav{stroke:#ff7500}[data-theme=cosma] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__account--placeholder-svg #Main-Mobile-Nav{stroke:#333333}.topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__sso-login__user-avatar:after,[data-theme=core] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__sso-login__user-avatar:after{border-color:#ff7500}[data-theme=cosma] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label .topnavigation__sso-login__user-avatar:after{border-color:#333}.topnavigation__overlay--account--show .topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label{border-bottom:0!important}[data-theme=cosma] .topnavigation__overlay--account--show .topnavigation__hover-tabs__label{border-bottom:3px solid #00ffd0!important}.topnavigation__hover-tabs__label:active,[data-theme=core] .topnavigation__hover-tabs__label:active{border-color:#ff7500}[data-theme=cosma] .topnavigation__hover-tabs__label:active{border-color:#333}}@media (min-width:1014px){.topnavigation__hover-tabs__label{padding-top:24px;padding-left:20px;padding-right:20px;padding-bottom:22px;font-size:14px;font-size:1.4rem}}@media (min-width:668px) and (max-width:830px){.topnavigation__hover-tabs__label{padding-left:10px;padding-right:0}}@media (min-width:669px){.topnavigation__sso-login .topnavigation__hover-tabs__label{padding-top:0;padding-bottom:0;border-bottom:none}.topnavigation__sso-login .topnavigation__hover-tabs__label,[data-theme=core] .topnavigation__sso-login .topnavigation__hover-tabs__label{max-height:63px}[data-theme=cosma] .topnavigation__sso-login .topnavigation__hover-tabs__label{max-height:66px}.topnavigation__sso-login.topnavigation__hover-layer{width:260px}.topnavigation__hover-tabs.topnavigation__sso-login>li.active .topnavigation__hover-tabs__label{box-shadow:none}}@media (min-width:669px){.topnavigation__hover-layer{position:absolute;z-index:2000;background-color:#fff;box-shadow:0 4px 4px -1px rgba(0,0,0,.2);display:flex;align-items:center;justify-content:center}.topnavigation__hover-layer{display:none;top:63px;border-top:1px solid #e0e0e0;border-bottom:1px solid #e0e0e0}.topnavigation__hover-layer.topnavigation__hover-layer--right-aligned{top:32px;left:auto;width:260px;position:absolute;border:1px solid #e0e0e0;display:none}.topnavigation__hover-layer a,.topnavigation__hover-layer ul a{color:#333}.topnavigation__hover-layer a:active:not(.button-primary),.topnavigation__hover-layer a:focus:not(.button-primary),.topnavigation__hover-layer a:hover:not(.button-primary),.topnavigation__hover-layer ul a:active:not(.button-primary),.topnavigation__hover-layer ul a:focus:not(.button-primary),.topnavigation__hover-layer ul a:hover:not(.button-primary),[data-theme=core] .topnavigation__hover-layer a:active:not(.button-primary),[data-theme=core] .topnavigation__hover-layer a:focus:not(.button-primary),[data-theme=core] .topnavigation__hover-layer a:hover:not(.button-primary),[data-theme=core] .topnavigation__hover-layer ul a:active:not(.button-primary),[data-theme=core] .topnavigation__hover-layer ul a:focus:not(.button-primary),[data-theme=core] .topnavigation__hover-layer ul a:hover:not(.button-primary){color:#ff7500}[data-theme=cosma] .topnavigation__hover-layer a:active:not(.button-primary),[data-theme=cosma] .topnavigation__hover-layer a:focus:not(.button-primary),[data-theme=cosma] .topnavigation__hover-layer a:hover:not(.button-primary),[data-theme=cosma] .topnavigation__hover-layer ul a:active:not(.button-primary),[data-theme=cosma] .topnavigation__hover-layer ul a:focus:not(.button-primary),[data-theme=cosma] .topnavigation__hover-layer ul a:hover:not(.button-primary){color:#333}.topnavigation__hover-layer .sso-login-link.link-underline,.topnavigation__hover-layer .topnavigation-last-search-notification__save-button.link-underline{color:#2267e8}.topnavigation :not(.sso-login) .topnavigation__hover-layer__navigation-wrapper{max-width:1170px;padding-left:40px}.topnavigation__level--2{max-height:0;opacity:0;overflow-y:hidden}.topnavigation__level--2 .grid-item{padding-left:16px;padding-right:16px}.topnavigation__menu-section--open+.topnavigation__level--2{max-height:1000px;opacity:1}.topnavigation__level--2__label{display:none}.topnavigation__level--3{margin-bottom:34px}.topnavigation__level--3 h3{color:#333;font-weight:600}.topnavigation__level--3 h3,.topnavigation__level--3 li{line-height:1.61;margin-bottom:8px;white-space:nowrap;overflow-x:hidden;text-overflow:ellipsis}}@media (min-width:669px) and (max-width:1013px){.topnavigation__level--2 .grid-item{max-width:203px}.topnavigation__level--3 h3,.topnavigation__level--3 li{font-size:14px;font-size:1.4rem}}@media (min-width:1014px){.topnavigation__level--3 h3{font-size:14px;font-size:1.4rem}.topnavigation__level--3 li{font-size:14px;font-size:1.4rem}}@media (max-width:668px){body.noscroll{overflow:hidden;position:fixed;width:100%;padding-top:96px}}@media (max-width:668px){.topnavigation__overlay--account .topnavigation__level--1{padding:16px 24px;width:100vw;background-color:#fff}.topnavigation__overlay--account .topnavigation-overlay-touch-area{display:block;padding-top:8px;padding-bottom:8px;padding-left:0;text-indent:0;color:#343434;font-size:1.4rem;font-weight:600;border-top:1px solid #e0e0e0}.topnavigation__overlay--account .topnavigation-overlay-touch-area:before{display:none}.topnavigation__overlay--account li:first-child>.topnavigation-overlay-touch-area{border-top:none}}@media (min-width:669px){.topnavigation__overlay-trigger--account,.topnavigation__overlay-trigger--menu{display:none}}@media (max-width:668px){.topnavigation__overlay-trigger--menu{position:absolute;top:0;left:0;padding:15px 16px}.topnavigation__overlay-trigger--menu .topnavigation__burger{width:24px;height:18px;position:relative;-webkit-transform:rotate(0);-moz-transform:rotate(0);-ms-transform:rotate(0);-o-transform:rotate(0);transform:rotate(0);-webkit-transition:.5s ease-in-out;-moz-transition:.5s ease-in-out;-o-transition:.5s ease-in-out;transition:.5s ease-in-out;cursor:pointer}.topnavigation__overlay-trigger--menu .topnavigation__burger span{display:block;position:absolute;height:2px;width:100%;background:#333;opacity:1;left:0;-webkit-transform:rotate(0);-moz-transform:rotate(0);-ms-transform:rotate(0);-o-transform:rotate(0);transform:rotate(0);-webkit-transition:.25s ease-in-out;-moz-transition:.25s ease-in-out;-o-transition:.25s ease-in-out;transition:.25s ease-in-out}.topnavigation__overlay-trigger--menu .topnavigation__burger span:first-child{top:0}.topnavigation__overlay-trigger--menu .topnavigation__burger span:nth-child(2),.topnavigation__overlay-trigger--menu .topnavigation__burger span:nth-child(3){top:8px}.topnavigation__overlay-trigger--menu .topnavigation__burger span:nth-child(4){top:16px}.topnavigation__overlay-trigger--menu.open .topnavigation__burger span:first-child,.topnavigation__overlay-trigger--menu.open .topnavigation__burger span:nth-child(4){top:8px;width:0;left:50%}.topnavigation__overlay-trigger--menu.open .topnavigation__burger span:nth-child(2){-webkit-transform:rotate(45deg);-moz-transform:rotate(45deg);-ms-transform:rotate(45deg);-o-transform:rotate(45deg);transform:rotate(45deg)}.topnavigation__overlay-trigger--menu.open .topnavigation__burger span:nth-child(3){-webkit-transform:rotate(-45deg);-moz-transform:rotate(-45deg);-ms-transform:rotate(-45deg);-o-transform:rotate(-45deg);transform:rotate(-45deg)}.topnavigation__overlay-trigger--account{right:16px;height:48px}.topnavigation--no-burger .topnavigation__overlay-trigger--account{right:12px}.topnavigation__overlay-trigger--account:focus,.topnavigation__overlay-trigger--account:hover,.topnavigation__overlay-trigger--menu:focus,.topnavigation__overlay-trigger--menu:hover{text-decoration:none}}@media (min-width:1014px){.topnavigation__sso-login{width:192px}}.topnavigation__sso-login .button-primary{padding:.45em .2em!important;text-decoration:none}.topnavigation__sso-login .button-primary,[data-theme=core] .topnavigation__sso-login .button-primary{border-radius:4px}[data-theme=cosma] .topnavigation__sso-login .button-primary{border-radius:8px}.topnavigation__sso-login .button-primary,.topnavigation__sso-login .button-primary:link,.topnavigation__sso-login .button-primary:visited,[data-theme=core] .topnavigation__sso-login .button-primary,[data-theme=core] .topnavigation__sso-login .button-primary:link,[data-theme=core] .topnavigation__sso-login .button-primary:visited{color:#fff}[data-theme=cosma] .topnavigation__sso-login .button-primary,[data-theme=cosma] .topnavigation__sso-login .button-primary:link,[data-theme=cosma] .topnavigation__sso-login .button-primary:visited{color:#333}.topnavigation__sso-login .button-primary,.topnavigation__sso-login .button-primary:link,.topnavigation__sso-login .button-primary:visited,[data-theme=core] .topnavigation__sso-login .button-primary,[data-theme=core] .topnavigation__sso-login .button-primary:link,[data-theme=core] .topnavigation__sso-login .button-primary:visited{border-color:#ff7500}[data-theme=cosma] .topnavigation__sso-login .button-primary,[data-theme=cosma] .topnavigation__sso-login .button-primary:link,[data-theme=cosma] .topnavigation__sso-login .button-primary:visited{border-color:#00ffd0}.topnavigation__sso-login .button-primary,.topnavigation__sso-login .button-primary:link,.topnavigation__sso-login .button-primary:visited,[data-theme=core] .topnavigation__sso-login .button-primary,[data-theme=core] .topnavigation__sso-login .button-primary:link,[data-theme=core] .topnavigation__sso-login .button-primary:visited{background-color:#ff7500}[data-theme=cosma] .topnavigation__sso-login .button-primary,[data-theme=cosma] .topnavigation__sso-login .button-primary:link,[data-theme=cosma] .topnavigation__sso-login .button-primary:visited{background-color:#00ffd0}.topnavigation__sso-login .button-primary:hover{text-decoration:none!important}.topnavigation__sso-login .button-primary:hover,[data-theme=core] .topnavigation__sso-login .button-primary:hover{color:#fff}[data-theme=cosma] .topnavigation__sso-login .button-primary:hover{color:#333}.topnavigation__sso-login .button-primary:hover,[data-theme=core] .topnavigation__sso-login .button-primary:hover{border-color:#eb6c00}[data-theme=cosma] .topnavigation__sso-login .button-primary:hover{border-color:#00f2c6}.topnavigation__sso-login .button-primary:hover,[data-theme=core] .topnavigation__sso-login .button-primary:hover{background-color:#eb6c00}[data-theme=cosma] .topnavigation__sso-login .button-primary:hover{background-color:#00f2c6}.topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login--logged-in,.topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__link-list--logged-in,.topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__user-avatar-logged-in{margin:auto 0}.topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login--logged-in,.topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__link-list--logged-in,.topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__user-avatar-logged-in,[data-theme=core] .topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login--logged-in,[data-theme=core] .topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__link-list--logged-in,[data-theme=core] .topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__user-avatar-logged-in,[data-theme=cosma] .topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login--logged-in,[data-theme=cosma] .topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__link-list--logged-in,[data-theme=cosma] .topnavigation__sso-login:not(.sso-login--logged-in) .topnavigation__sso-login__user-avatar-logged-in{display:none!important}.topnavigation__sso-login.sso-login--logged-in *{color:#333}.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login--logged-out,.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__link-list--logged-out,.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__user-avatar:not(.topnavigation__sso-login__user-avatar-logged-in){margin:auto 0}.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login--logged-out,.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__link-list--logged-out,.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__user-avatar:not(.topnavigation__sso-login__user-avatar-logged-in),[data-theme=core] .topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login--logged-out,[data-theme=core] .topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__link-list--logged-out,[data-theme=core] .topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__user-avatar:not(.topnavigation__sso-login__user-avatar-logged-in),[data-theme=cosma] .topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login--logged-out,[data-theme=cosma] .topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__link-list--logged-out,[data-theme=cosma] .topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__user-avatar:not(.topnavigation__sso-login__user-avatar-logged-in){display:none!important}.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login--logged-in{display:flex;flex-direction:column;margin:auto 0}.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login--logged-in>span{font-weight:400}.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login--logged-in .topnavigation__sso-login__user-name{line-height:22px;font-weight:700;max-width:138px;text-overflow:ellipsis;overflow:hidden;white-space:nowrap}.topnavigation__sso-login.sso-login--logged-in .topnavigation__sso-login__user-avatar:not(.topnavigation_sso-login_private) .icon{display:none}.topnavigation__sso-login:not(.sso-login--show-avatar) .topnavigation__sso-login__user-avatar,[data-theme=core] .topnavigation__sso-login:not(.sso-login--show-avatar) .topnavigation__sso-login__user-avatar,[data-theme=cosma] .topnavigation__sso-login:not(.sso-login--show-avatar) .topnavigation__sso-login__user-avatar{display:none!important}:not(.topnavigation__notification--present) .topnavigation-last-search-teaser,[data-theme=core] :not(.topnavigation__notification--present) .topnavigation-last-search-teaser,[data-theme=cosma] :not(.topnavigation__notification--present) .topnavigation-last-search-teaser{display:none!important}@media (max-width:668px){.sso-login-link,[data-theme=core] .sso-login-link{color:#ff7500}[data-theme=cosma] .sso-login-link{color:#000}.sso-login-link>div>.topnavigation-last-search-notification{visibility:hidden}}.topnavigation__sso-login__welcome-message{padding-bottom:2px;font-size:1.2rem;font-weight:400}@media (min-width:669px){.topnavigation__sso-login__welcome-message{font-size:1.2rem}}@media (max-width:668px){.topnavigation__sso-login__welcome-message{max-width:14em}}@media (min-width:669px){.topnavigation__sso-login__welcome-message{max-width:6em}}@media (min-width:1014px){.topnavigation__sso-login__welcome-message{max-width:10em}}.topnavigation__sso-login__label-text-wrapper,.topnavigation__sso-login__user-avatar{display:inline-block;vertical-align:middle}@media (max-width:668px){.topnavigation__overlay-trigger--account .topnavigation__sso-login__user-avatar{display:inline-block}.topnavigation__overlay-trigger--account .sso-login__user-name{display:none}}@media (max-width:1400px){.topnavigation__sso-login .topnavigation__sso-login__label-text-wrapper{display:none}}@media (min-width:1400px){[data-theme=cosma] .topnavigation__sso-login__label-text-wrapper .topnavigation__chevronAppend--desktop:after{border-style:solid;border-width:.107em .107em 0 0;content:'';display:inline-block;height:.5em;left:3px;position:relative;transform:rotate(135deg);vertical-align:top;width:.5em;top:.1em}}.topnavigation__sso-login__user-avatar{background-color:#fff}.topnavigation__sso-login__user-avatar,[data-theme=core] .topnavigation__sso-login__user-avatar,[data-theme=cosma] .topnavigation__sso-login__user-avatar{overflow:visible!important}.topnavigation__sso-login__user-avatar>a>svg{vertical-align:middle}.topnavigation__sso-login__user-avatar img{width:100%;height:100%}.topnavigation__sso-login__user-avatar.topnavigation__hasAvatar{border-radius:50%;border:2px solid #00ffd0;margin-right:0!important;overflow:hidden!important}.topnavigation__sso-login__user-avatar.topnavigation__hasAvatar,[data-theme=core] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar,[data-theme=cosma] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar{margin-left:0!important}.topnavigation__sso-login__user-avatar.topnavigation__hasAvatar,[data-theme=core] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar,[data-theme=cosma] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar{top:20px!important}@media (min-width:1014px){.topnavigation__sso-login__user-avatar.topnavigation__hasAvatar,[data-theme=core] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar,[data-theme=cosma] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar{top:16px!important}}.topnavigation__sso-login__user-avatar.topnavigation__hasAvatar .topnavigation__account--placeholder-svg-core,.topnavigation__sso-login__user-avatar.topnavigation__hasAvatar .topnavigation__account--placeholder-svg-cosma,[data-theme=core] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar .topnavigation__account--placeholder-svg-core,[data-theme=core] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar .topnavigation__account--placeholder-svg-cosma,[data-theme=cosma] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar .topnavigation__account--placeholder-svg-core,[data-theme=cosma] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar .topnavigation__account--placeholder-svg-cosma{display:none!important}.topnavigation__sso-login__user-avatar.topnavigation__hasAvatar.topnavigation__hasAvatar--plus,[data-theme=core] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar.topnavigation__hasAvatar--plus,[data-theme=cosma] .topnavigation__sso-login__user-avatar.topnavigation__hasAvatar.topnavigation__hasAvatar--plus{border-color:#00ffd0!important}.topnavigation__overlay--account__hide{display:block}.topnavigation__overlay-trigger--account:hover,[data-theme=core] .topnavigation__overlay-trigger--account:hover,[data-theme=cosma] .topnavigation__overlay-trigger--account:hover{color:#606060!important}@media (max-width:668px){.topnavigation__overlay--account__hide{display:none}.topnavigation__overlay-trigger--account,[data-theme=core] .topnavigation__overlay-trigger--account,[data-theme=cosma] .topnavigation__overlay-trigger--account{color:#606060!important}.topnavigation__overlay-trigger--account .topnavigation__sso-login__label-text-wrapper{color:#343434;font-weight:600;font-size:1.4rem;line-height:1.4rem}.topnavigation__overlay-trigger--account .sso-login__user-name{color:#4c4c4c;font-weight:600;font-size:1rem;max-width:70px}}.top-navigation__button{height:32px;line-height:16px!important}.top-navigation__button,[data-theme=core] .top-navigation__button{font-family:"Open Sans",Verdana,"DejaVu Sans",Arial,Helvetica,sans-serif}[data-theme=cosma] .top-navigation__button{font-family:"Make It Sans IS24 Web",Verdana,"DejaVu Sans",Arial,Helvetica,sans-serif}@media (max-width:1013px){.top-navigation__anbieten-button-teaser{display:none!important}.top-navigation__anbieten-button{background-color:#fff;color:#343434;padding:.45em 12px!important;font-size:1.4rem}.top-navigation__anbieten-button,[data-theme=core] .top-navigation__anbieten-button{border-radius:3px}[data-theme=cosma] .top-navigation__anbieten-button{border-radius:8px}.top-navigation__anbieten-button,.top-navigation__anbieten-button:link,.top-navigation__anbieten-button:visited{box-shadow:none;background:0 0;filter:none;text-shadow:none;background-color:#fff;color:#343434}.top-navigation__anbieten-button,.top-navigation__anbieten-button:link,.top-navigation__anbieten-button:visited,[data-theme=core] .top-navigation__anbieten-button,[data-theme=core] .top-navigation__anbieten-button:link,[data-theme=core] .top-navigation__anbieten-button:visited{border-color:#676767}[data-theme=cosma] .top-navigation__anbieten-button,[data-theme=cosma] .top-navigation__anbieten-button:link,[data-theme=cosma] .top-navigation__anbieten-button:visited{border-color:#676767}}@media (min-width:1014px){.top-navigation__anbieten-button-teaser{display:block;font-size:1.4rem;margin-right:20px;padding:.45em 18px!important}}@media (min-width:669px){.top-navigation__anbieten-button{padding:.45em 12px!important;font-size:1.4rem}.top-navigation__anbieten-button,[data-theme=core] .top-navigation__anbieten-button{border-radius:3px}[data-theme=cosma] .top-navigation__anbieten-button{border-radius:8px}.top-navigation__anbieten-button,.top-navigation__anbieten-button:link,.top-navigation__anbieten-button:visited{box-shadow:none;background:0 0;filter:none;text-shadow:none;background-color:#fff;color:#343434}.top-navigation__anbieten-button,.top-navigation__anbieten-button:link,.top-navigation__anbieten-button:visited,[data-theme=core] .top-navigation__anbieten-button,[data-theme=core] .top-navigation__anbieten-button:link,[data-theme=core] .top-navigation__anbieten-button:visited{border-color:#676767}[data-theme=cosma] .top-navigation__anbieten-button,[data-theme=cosma] .top-navigation__anbieten-button:link,[data-theme=cosma] .top-navigation__anbieten-button:visited{border-color:#676767}.top-navigation__anbieten-button:active,.top-navigation__anbieten-button:focus,.top-navigation__anbieten-button:hover,[data-theme=core] .top-navigation__anbieten-button:active,[data-theme=core] .top-navigation__anbieten-button:focus,[data-theme=core] .top-navigation__anbieten-button:hover{color:#3d648c}[data-theme=cosma] .top-navigation__anbieten-button:active,[data-theme=cosma] .top-navigation__anbieten-button:focus,[data-theme=cosma] .top-navigation__anbieten-button:hover{color:#333}.top-navigation__anbieten-button:active,.top-navigation__anbieten-button:focus,.top-navigation__anbieten-button:hover,[data-theme=core] .top-navigation__anbieten-button:active,[data-theme=core] .top-navigation__anbieten-button:focus,[data-theme=core] .top-navigation__anbieten-button:hover{background-color:#f2f2f2}[data-theme=cosma] .top-navigation__anbieten-button:active,[data-theme=cosma] .top-navigation__anbieten-button:focus,[data-theme=cosma] .top-navigation__anbieten-button:hover{background-color:#f5f5f5}.topnavigation__overlay--menu button{width:100%;padding:.64285714em 0}}html{touch-action:manipulation}.sidebarnavigation__divider{height:1px;background-color:#eaeaea}.sidebarnavigation__logo{display:block}#sidebarnavigation-slide-submenu{height:0;flex-wrap:nowrap;opacity:0;background-color:#fff;background-clip:content-box}#sidebarnavigation-slide-submenu.open{height:100%;opacity:1}.sidebarnavigation-submenu-heading:not(.active).link-container>.link{font-weight:400}.sidebarnavigation-submenu-heading:not(.active) .sidebarnavigation-submenu-links{transition:opacity ease-in .5s,max-height ease-in-out .5s;max-height:0;opacity:0}.sidebarnavigation-submenu-heading:not(.active) .accordion{transition:all .3s}.sidebarnavigation-submenu-heading>.accordion{margin:auto 0}.sidebarnavigation-submenu-heading>.accordion:before{vertical-align:middle}.sidebarnavigation-submenu-heading.active>.accordion{transform:rotate(180deg);transition:all .5s}.sidebarnavigation-submenu-heading.active .sidebarnavigation-submenu-links{opacity:1;max-height:100vh;transition:opacity ease-in-out .4s,max-height ease-in-out .7s}.sidebarnavigation__slide-menu{height:0;position:fixed;top:0;opacity:0;background-color:#fff;z-index:9999}.sidebarnavigation__slide-menu.open{height:100%;opacity:1}.sidebarnavigation-overlay{height:0;position:fixed;top:0;left:0;background-color:rgba(0,0,0,.5);opacity:0;pointer-events:none;transition:opacity .5s ease-in-out,height .5s step-end;z-index:9998}.sidebarnavigation-overlay.open{height:100%;opacity:1;pointer-events:auto;transition:opacity .5s ease-in-out}@media (min-width:1014px){.sidebarnavigation-menu--secondary:not(.active):hover.link-container>.link{text-underline-offset:10px!important}.sidebarnavigation-menu--secondary>a{color:#333!important;text-decoration:none!important}.sidebarnavigation__logo>img{width:137px}.sidebarnavigation-menu{max-height:500px;overflow:hidden}.sidebarnavigation__slide-menu{left:-100%;transition:left .5s ease-in-out,opacity ease-in .5s,height step-end .5s}.sidebarnavigation__slide-menu #sidebarnavigation-slide-submenu{left:100%;transition:left .5s ease-in-out,opacity step-end .5s,height step-end .5s,padding-left step-end .5s}.sidebarnavigation__slide-menu #sidebarnavigation-slide-submenu.open{left:0;transition:left .5s ease-in-out,opacity step-start,height step-start}.sidebarnavigation__slide-menu.open{left:0;overflow-y:auto;transition:left .5s ease-in-out,opacity ease-out .5s,height step-start}.sidebarnavigation-submenu-heading,.sidebarnavigation__headlines{width:263px}}@media (min-width:1014px) and (max-width:1169px){.sidebarnavigation__slide-menu{padding-left:32px}.sidebarnavigation__slide-menu #sidebarnavigation-slide-submenu.open{padding-left:32px}}@media (min-width:1014px) and (min-width:1170px) and (max-width:1313px){.sidebarnavigation__slide-menu{padding-left:calc((100vw - 1170px)/ 2 + 32px)}.sidebarnavigation__slide-menu #sidebarnavigation-slide-submenu.open{padding-left:calc((100vw - 1170px)/ 2 + 32px)}}@media (min-width:1014px) and (min-width:1314px){.sidebarnavigation__slide-menu{padding-left:calc((100vw - 1170px)/ 2 + 32px);margin-left:-72px}.sidebarnavigation__slide-menu #sidebarnavigation-slide-submenu.open{padding-left:calc((100vw - 1170px)/ 2 + 32px)}}@media (max-width:1013px){.sidebarnavigation__slide-menu{transition:right .5s ease-in-out,opacity ease-in .5s,height step-end .5s}.sidebarnavigation__slide-menu.open{right:0;transition:right .5s ease-in-out,opacity ease-out .5s,height step-start}#sidebarnavigation-slide-submenu{right:-100%;transition:right .5s ease-in-out,opacity step-end .5s,height step-end .5s}#sidebarnavigation-slide-submenu.open{right:0;transition:right .5s ease-in-out,opacity step-start,height step-start}.disallowScroll{overflow:hidden}}@media (min-width:669px) and (max-width:1013px){.sidebarnavigation__closebtn:hover{cursor:pointer}.sidebarnavigation__slide-menu{right:-100%;width:calc(100vw / 2)}}@media (max-width:668px){.sidebarnavigation__slide-menu{right:-100%;width:315px}}.topnavigation-flyout{margin-top:-14px}@media (max-width:668px){.topnavigation-flyout{padding-top:10px}}.topnavigation-flyout__toggler{margin:0 -24px!important;width:auto!important}.topnavigation-flyout__toggler,[data-theme=core] .topnavigation-flyout__toggler{flex-flow:row wrap}[data-theme=cosma] .topnavigation-flyout__toggler{flex-flow:row nowrap}@media (min-width:669px){.topnavigation-flyout__toggler{margin:0!important}}.topnavigation-flyout__toggler a{text-decoration:none}.topnavigation-flyout__toggler__toggle{border-bottom:none}.topnavigation-flyout__toggler__toggle,[data-theme=core] .topnavigation-flyout__toggler__toggle{height:41px}[data-theme=cosma] .topnavigation-flyout__toggler__toggle{height:40px}.topnavigation-flyout__toggler__toggle,[data-theme=core] .topnavigation-flyout__toggler__toggle{line-height:41px}[data-theme=cosma] .topnavigation-flyout__toggler__toggle{line-height:40px}.topnavigation-flyout__toggler__toggle,[data-theme=core] .topnavigation-flyout__toggler__toggle{background-color:#f2f2f2}[data-theme=cosma] .topnavigation-flyout__toggler__toggle{background-color:#f5f5f5}.topnavigation-flyout__toggler__toggle,[data-theme=core] .topnavigation-flyout__toggler__toggle{color:#545454}[data-theme=cosma] .topnavigation-flyout__toggler__toggle{color:#333}.topnavigation-flyout__toggler__toggle,[data-theme=core] .topnavigation-flyout__toggler__toggle{font-weight:400}[data-theme=cosma] .topnavigation-flyout__toggler__toggle{font-weight:600}.topnavigation-flyout__toggler__toggle--consumer:hover,.topnavigation-flyout__toggler__toggle--provider:hover{cursor:pointer}.topnavigation-flyout__toggler__toggle--consumer:hover,.topnavigation-flyout__toggler__toggle--provider:hover,[data-theme=core] .topnavigation-flyout__toggler__toggle--consumer:hover,[data-theme=core] .topnavigation-flyout__toggler__toggle--provider:hover{font-weight:700}[data-theme=cosma] .topnavigation-flyout__toggler__toggle--consumer:hover,[data-theme=cosma] .topnavigation-flyout__toggler__toggle--provider:hover{font-weight:600}.topnavigation-flyout__toggler__toggle--consumer:hover,.topnavigation-flyout__toggler__toggle--provider:hover,[data-theme=core] .topnavigation-flyout__toggler__toggle--consumer:hover,[data-theme=core] .topnavigation-flyout__toggler__toggle--provider:hover{background-color:#eee}[data-theme=cosma] .topnavigation-flyout__toggler__toggle--consumer:hover,[data-theme=cosma] .topnavigation-flyout__toggler__toggle--provider:hover{background-color:#f5f5f5}.topnavigation-flyout__toggler__toggle--selected{height:40px;line-height:40px;background-color:#fff!important;font-weight:600}.topnavigation-flyout__toggler__toggle--selected,[data-theme=core] .topnavigation-flyout__toggler__toggle--selected{color:#242424}[data-theme=cosma] .topnavigation-flyout__toggler__toggle--selected{color:#333}.topnavigation-flyout__toggler__toggle--selected:hover{cursor:pointer}.topnavigation-flyout__toggler__toggle--selected::after{content:'';display:block;background:#00ffd0;width:75%;height:4px;margin:0 auto;margin-top:-4px}@media (min-width:669px){.topnavigation-flyout__menu-items{padding:0 24px}}.topnavigation-flyout__menu-items li a,.topnavigation-flyout__menu-items li a:link{font-weight:400;text-decoration:none}@media (max-width:668px){.topnavigation-flyout__menu-items li a,.topnavigation-flyout__menu-items li a:link{font-size:13px;font-weight:400;text-decoration:none}.topnavigation-flyout__menu-items li a,.topnavigation-flyout__menu-items li a:link,[data-theme=core] .topnavigation-flyout__menu-items li a,[data-theme=core] .topnavigation-flyout__menu-items li a:link{color:#262626}[data-theme=cosma] .topnavigation-flyout__menu-items li a,[data-theme=cosma] .topnavigation-flyout__menu-items li a:link{color:#333}}.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-membership,[data-theme=core] .topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-membership{color:#ff7501}[data-theme=cosma] .topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-membership{color:#333}.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-membership:hover,[data-theme=core] .topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-membership:hover{text-decoration:underline}[data-theme=cosma] .topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-membership:hover{text-decoration:none}.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__plus-membership::before,.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__plus-profile::after,.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-icon::before{width:37px;height:20px;margin-bottom:2px;content:'';display:inline-block;background:url('https://www.static-immobilienscout24.de/statpic/plus-badge/6036b61cd7c3a7f4de0e79c5387f177f_dark.svg') no-repeat center center;background-size:contain;vertical-align:middle}.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__plus-membership::before,.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__premium-icon::before{margin-right:3px}.topnavigation-flyout__menu-items .topnavigation-flyout__menu-items__plus-profile::after{margin-left:6px}[data-theme=core] .topnavigation-flyout__logout-option li{padding-top:10px;border-top:1px solid #e0e0e0;font-size:14px}[data-theme=core] .topnavigation-flyout__logout-option li,[data-theme=core] [data-theme=core] .topnavigation-flyout__logout-option li{border-top:1px solid #e0e0e0}[data-theme=cosma] [data-theme=core] .topnavigation-flyout__logout-option li{border-top:none}@media (max-width:768px){[data-theme=core] .topnavigation-flyout__logout-option li{font-size:13px}}[data-theme=core] .topnavigation-flyout__logout-option a{color:#242424;text-decoration:none}.topnavigation__sso-login__link-list.topnavigation-flyout__provider-option>li{border-top:1px solid #e0e0e0}.sso-login__link--logged-in{display:none}.sso-login--logged-in .sso-login__link--logged-out{display:none}.sso-login--logged-in .sso-login__link--logged-in{display:block}.page-header__brand{font-weight:400}.page-header__brand,[data-theme=core] .page-header__brand{color:#747474}[data-theme=cosma] .page-header__brand{color:#606060}.page-header--white--2016,.page-header.page-header--white--2016{border-bottom:1px solid #e0e0e0!important}.page-header--white--2016 .sso-login-link,.page-header.page-header--white--2016 .sso-login-link,[data-theme=core] .page-header--white--2016 .sso-login-link,[data-theme=core] .page-header.page-header--white--2016 .sso-login-link{color:#2a7cca!important}[data-theme=cosma] .page-header--white--2016 .sso-login-link,[data-theme=cosma] .page-header.page-header--white--2016 .sso-login-link{color:#0b3293!important}.page-header--white--2016 .sso-login-link:hover,.page-header.page-header--white--2016 .sso-login-link:hover,[data-theme=core] .page-header--white--2016 .sso-login-link:hover,[data-theme=core] .page-header.page-header--white--2016 .sso-login-link:hover{color:#ff7500!important}[data-theme=cosma] .page-header--white--2016 .sso-login-link:hover,[data-theme=cosma] .page-header.page-header--white--2016 .sso-login-link:hover{color:#0b3293!important}.page-header--white--2016 .sso-login-link::before,.page-header.page-header--white--2016 .sso-login-link::before,[data-theme=core] .page-header--white--2016 .sso-login-link::before,[data-theme=core] .page-header.page-header--white--2016 .sso-login-link::before{color:#ff851d!important}[data-theme=cosma] .page-header--white--2016 .sso-login-link::before,[data-theme=cosma] .page-header.page-header--white--2016 .sso-login-link::before{color:#0b3293!important}.page-header--white--composite .page-header__brand,.page-header.page-header--white--composite .page-header__brand{line-height:1.2}.page-header--white--composite .page-header__brand,.page-header.page-header--white--composite .page-header__brand,[data-theme=core] .page-header--white--composite .page-header__brand,[data-theme=core] .page-header.page-header--white--composite .page-header__brand{color:#003468}[data-theme=cosma] .page-header--white--composite .page-header__brand,[data-theme=cosma] .page-header.page-header--white--composite .page-header__brand{color:#333}.page-header--white--composite .page-header__logo>img,.page-header.page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header.page-header--white--composite .page-header__logo>img{width:64px!important}[data-theme=cosma] .page-header--white--composite .page-header__logo>img,[data-theme=cosma] .page-header.page-header--white--composite .page-header__logo>img{width:116px!important}.page-header--white--composite .page-header__logo>img,.page-header.page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header.page-header--white--composite .page-header__logo>img{height:32px!important}[data-theme=cosma] .page-header--white--composite .page-header__logo>img,[data-theme=cosma] .page-header.page-header--white--composite .page-header__logo>img{height:32px!important}@media (max-width:768px){.page-header--white--composite,.page-header.page-header--white--composite{position:relative;padding-top:8px;height:48px!important}}@media (min-width:1014px){.page-header--white--composite .page-header__logo>img,.page-header.page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header.page-header--white--composite .page-header__logo>img{width:80px!important}[data-theme=cosma] .page-header--white--composite .page-header__logo>img,[data-theme=cosma] .page-header.page-header--white--composite .page-header__logo>img{width:116px!important}.page-header--white--composite .page-header__logo>img,.page-header.page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header--white--composite .page-header__logo>img,[data-theme=core] .page-header.page-header--white--composite .page-header__logo>img{height:40px!important}[data-theme=cosma] .page-header--white--composite .page-header__logo>img,[data-theme=cosma] .page-header.page-header--white--composite .page-header__logo>img{height:32px!important}.page-header--white--composite,.page-header.page-header--white--composite{padding-top:5px!important;height:72px!important}}@media (min-width:669px){.topnavigation__vertical-align-center{padding:15px 0;height:64px}}@media (max-width:668px){.topnavigation__layer--is-open .palm-topnavigation-move-to-background{z-index:-1!important}}.noselect{-webkit-touch-callout:none;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.core-hide,[data-theme=core] .core-hide{display:none}[data-theme=cosma] .core-hide{display:initial}.cosma-hide,[data-theme=core] .cosma-hide{display:initial}[data-theme=cosma] .cosma-hide{display:none}@media (min-width:669px){.only-lap-and-up-content-wrapper{margin:0 auto;padding:0 16px;max-width:1170px}.only-lap-and-up-grid{display:block}.only-lap-and-up-grid:after{display:table;clear:both;content:""}.only-lap-and-up-grid-flex{display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:-ms-flex;display:flex;-webkit-flex-flow:row wrap;-moz-flex-flow:row wrap;-ms-flex-flow:row wrap;flex-flow:row wrap}.only-lap-and-up-grid-flex>.grid-item{-webkit-flex:0 1 auto;-moz-flex:0 1 auto;-ms-flex:0 1 auto;flex:0 1 auto;width:auto}.only-lap-and-up-grid-flex>.grid-item-fixed-width{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;-ms-box-sizing:content-box;-o-box-sizing:content-box;box-sizing:content-box}.only-lap-and-up-grid-flex.only-lap-and-up-grid-fill-rows>.grid-item:not(.grid-item-fixed-width){-webkit-flex:1 1 auto;-moz-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}.only-lap-and-up-grid-flex.gutter,.only-lap-and-up-grid-flex.gutter-vertical{margin-top:-24px}.only-lap-and-up-grid-flex.gutter-vertical>.grid-item,.only-lap-and-up-grid-flex.gutter>.grid-item{margin-top:24px;margin-bottom:0}.only-lap-and-up-grid-flex.gutter-vertical-xs,.only-lap-and-up-grid-flex.gutter-xs{margin-top:-4px}.only-lap-and-up-grid-flex.gutter-vertical-xs>.grid-item,.only-lap-and-up-grid-flex.gutter-xs>.grid-item{margin-top:4px;margin-bottom:0}.only-lap-and-up-grid-flex.gutter-s,.only-lap-and-up-grid-flex.gutter-vertical-s{margin-top:-8px}.only-lap-and-up-grid-flex.gutter-s>.grid-item,.only-lap-and-up-grid-flex.gutter-vertical-s>.grid-item{margin-top:8px;margin-bottom:0}.only-lap-and-up-grid-flex.gutter-m,.only-lap-and-up-grid-flex.gutter-vertical-m{margin-top:-16px}.only-lap-and-up-grid-flex.gutter-m>.grid-item,.only-lap-and-up-grid-flex.gutter-vertical-m>.grid-item{margin-top:16px;margin-bottom:0}.only-lap-and-up-grid-flex.gutter-l,.only-lap-and-up-grid-flex.gutter-vertical-l{margin-top:-24px}.only-lap-and-up-grid-flex.gutter-l>.grid-item,.only-lap-and-up-grid-flex.gutter-vertical-l>.grid-item{margin-top:24px;margin-bottom:0}.only-lap-and-up-grid-flex.gutter-vertical-xl,.only-lap-and-up-grid-flex.gutter-xl{margin-top:-32px}.only-lap-and-up-grid-flex.gutter-vertical-xl>.grid-item,.only-lap-and-up-grid-flex.gutter-xl>.grid-item{margin-top:32px;margin-bottom:0}.only-lap-and-up-grid-flex.gutter-vertical-xxl,.only-lap-and-up-grid-flex.gutter-xxl{margin-top:-40px}.only-lap-and-up-grid-flex.gutter-vertical-xxl>.grid-item,.only-lap-and-up-grid-flex.gutter-xxl>.grid-item{margin-top:40px;margin-bottom:0}.only-lap-and-up-grid-flex.only-lap-and-up-grid-fill-rows>.only-lap-and-up-grid-item:not(.only-lap-and-up-grid-item-fixed-width){-webkit-flex:1 1 auto;-moz-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}.only-lap-and-up-grid-item{display:block;float:left;width:100%;vertical-align:top;text-align:left}.only-lap-and-up-grid-flex>.only-lap-and-up-grid-item{-webkit-flex:0 1 auto;-moz-flex:0 1 auto;-ms-flex:0 1 auto;flex:0 1 auto;width:auto}.only-lap-and-up-grid-flex>.only-lap-and-up-grid-item-fixed-width{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;-ms-box-sizing:content-box;-o-box-sizing:content-box;box-sizing:content-box}.only-lap-and-up-grid-flex.grid-fill-rows>.only-lap-and-up-grid-item:not(.only-lap-and-up-grid-item-fixed-width){-webkit-flex:1 1 auto;-moz-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}.only-lap-and-up-grid-align-center{-ms-flex-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;align-items:center;-webkit-align-self:center;-moz-align-self:center;-ms-align-self:center;align-self:center}.only-lap-and-up-grid-flex>.only-lap-and-up-grid-item-fixed-width{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;-ms-box-sizing:content-box;-o-box-sizing:content-box;box-sizing:content-box}.only-lap-and-up-grid-flex.only-lap-and-up-grid-fill-rows>.only-lap-and-up-grid-item:not(.only-lap-and-up-grid-item-fixed-width){-webkit-flex:1 1 auto;-moz-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}.only-lap-and-up-grid-justify-end{-ms-flex-pack:end;-webkit-justify-content:flex-end;-moz-justify-content:flex-end;-ms-justify-content:flex-end;justify-content:flex-end}.only-lap-and-up-order-two-down{-webkit-order:2;-moz-order:2;-ms-flex-order:2;-ms-order:2;order:2}.only-lap-and-up-order-one-down{-webkit-order:1;-moz-order:1;-ms-flex-order:1;-ms-order:1;order:1}}@media (min-width:669px) and (min-width:1px){.only-lap-and-up-grid-flex:after{content:none}}</style><script src="https://app.usercentrics.eu/browser-ui/latest/loader.js" type="text/javascript" id="usercentrics-cmp" data-tcf-enabled="true" data-settings-id="Zj3Me6gb1" data-avoid-prefetch-services=""></script><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.monthly-rate-tooltip-container {
  opacity: 1 !important;
}
@media (max-width: 668px) {
  .monthly-rate-tooltip-container {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0 !important;
    top: 0 !important;
    background-color: white !important;
    margin-top: 0 !important;
    z-index: 100000;
  }
}
.monthly-rate-tooltip-container .tooltip-arrow {
  border: 1px solid !important;
  border-color: #e0e0e0 #e0e0e0 transparent transparent !important;
  height: 10px;
  width: 10px;
  background-color: white;
  transform: rotate(-45deg);
}
.monthly-rate-tooltip-container .tooltip-inner {
  max-width: 100%;
}
@media (min-width: 669px) {
  .monthly-rate-tooltip-container .tooltip-inner {
    border: 1px solid #e0e0e0 !important;
    box-shadow: 0 4px 16px 0 rgba(0, 0, 0, 0.1);
    max-width: 293px;
    padding: 0;
  }
}
.monthly-rate-tooltip-container .monthly-rate-content-div > .grid-item {
  margin-bottom: 16px;
}
@media (max-width: 668px) {
  .monthly-rate-tooltip-container .monthly-rate-content-div {
    padding-top: 40px !important;
    padding-left: 55px !important;
    padding-right: 55px !important;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.mapContainer {
  position: relative;
  width: 100%;
  height: 450px;
}
@media (min-height: 600px) {
  .mapContainer.mapContainerLarge {
    height: calc(100vh - 120px) !important;
    min-height: 450px;
  }
}
.mapContainer.mapContainerControlsTop {
  border-top: 1px solid #d4d4d4;
}
.mapContainer.mapContainerControlsBottom {
  border-bottom: 1px solid #d4d4d4;
}
.legendContainer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #fafafa;
}
@media (min-width: 669px) {
  .mapControls {
    min-height: 80px;
  }
}
@media (max-width: 668px) {
  .mapControls {
    padding-top: 8px;
    padding-bottom: 8px;
  }
}
.mapControls .mapControlOuter {
  padding-top: 20px;
  padding-bottom: 18px;
}
@media (max-width: 668px) {
  .mapControls .mapControlOuter {
    padding-top: 8px;
    padding-bottom: 8px;
  }
}
.mapControls .mapControlOuter button {
  background-color: white;
}
.mapControls.mapControlsTop {
  background-color: #fafafa;
}
.mapControls.mapControlsTop button {
  background-color: #fafafa !important;
}
.activeFeatureArrow {
  position: absolute;
  top: -1px;
  width: 12px;
  height: 10px;
  background: url("https://www.static-immobilienscout24.de/statpic/expose/icons/df50eaa0eafed348f76b7b7191c7f0fe_KB-Test.png");
  left: 50% !important;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
}
@media (max-width: 668px) {
  .activeFeatureArrow {
    display: none;
  }
}
.activeFeatureLine {
  position: absolute;
  bottom: 15px;
  min-width: 70px;
  height: 4px;
  background-color: #00ffd0;
  left: 50% !important;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  overflow: hidden;
  color: #fafafa;
}
@media (max-width: 668px) {
  .activeFeatureLine {
    bottom: 4px;
  }
}
.inactiveFeatureLine {
  position: absolute;
  bottom: 15px;
  min-width: 40px;
  height: 2px;
  background-color: #fafafa;
  left: 50% !important;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  color: #fafafa;
}
@media (max-width: 668px) {
  .inactiveFeatureLine {
    bottom: 4px;
  }
}
.mapMain {
  width: 100%;
  height: 100%;
}
.popupButtonList button {
  padding: 0;
}
.popupButtonList button span {
  vertical-align: top;
  padding-left: 8px;
}
.deactivateControlsBottom {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.featureIconButton__fill,
.featureIconButton__stroke,
.featureIconButton__fill__active,
.featureIconButton__stroke__active,
.featureIconButton__fill:hover,
.featureIconButton__stroke:hover,
.featureIconButton__fill__active:hover,
.featureIconButton__stroke__active:hover {
  text-decoration: none;
  outline: none;
}
button.featureIconButton__fill,
button.featureIconButton__stroke,
button.featureIconButton__fill__active,
button.featureIconButton__stroke__active {
  min-width: 7.2rem;
  padding-bottom: 6px;
}
button.featureIconButton__fill {
  color: #8f8f8f;
  fill: #8f8f8f;
}
button.featureIconButton__fill__active {
  color: #333333;
  fill: #333333;
}
button.featureIconButton__stroke__active {
  color: #333333;
  stroke: #333333;
}
button.featureIconButton__stroke {
  color: #8f8f8f;
  stroke: #8f8f8f;
}
button.featureIconButton__fill:hover {
  color: #333333;
  fill: #333333;
  cursor: pointer;
}
button.featureIconButton__stroke:hover {
  color: #333333;
  stroke: #333333;
  cursor: pointer;
}
@media (hover: none), (hover: on-demand) {
  button.featureIconButton__fill:hover {
    color: #343434;
    fill: #343434;
  }
  button.featureIconButton__stroke:hover {
    color: #343434;
    stroke: #343434;
  }
}
.buttonActive {
  color: #ff7400;
}
.listPopupEntries {
  max-height: calc(100% - 50px);
  overflow-y: auto;
  width: 100%;
}
.listPopupEntries li {
  padding-top: 8px!important;
  padding-bottom: 8px!important;
}
.listPopupEntries li:first-child {
  padding-top: 0;
}
.smallMobileLegend {
  overflow-x: scroll;
}
.smallMobileLegend ul {
  width: 2000px;
}
.smallMobileLegend ul li {
  float: left;
}
.expandLegendButton {
  border-left: 1px solid #cacaca;
}
.gradientContainer {
  position: absolute;
  right: 12.5%;
  top: 0;
  width: 30px;
  height: 40px;
  color: #cacaca;
  background: -webkit-linear-gradient(to right, rgba(242, 242, 242, 0), #f2f2f2);
  background: -moz-linear-gradient(to right, rgba(242, 242, 242, 0), #f2f2f2);
  background: -ms-linear-gradient(to right, rgba(242, 242, 242, 0), #f2f2f2);
  background: -o-linear-gradient(to right, rgba(242, 242, 242, 0), #f2f2f2);
  background: linear-gradient(to right, rgba(242, 242, 242, 0), #f2f2f2);
}
.mobileLargeHeader {
  margin-bottom: 32px;
}
.mapHeightToggle {
  outline: none;
}
@media (max-height: 599px) {
  .mapHeightToggle {
    display: none;
  }
}
@media (min-height: 600px) {
  .mapHeightToggle {
    display: inline-block;
    margin-right: 10px;
    width: 28px;
    height: 34px;
    border-radius: 2px;
  }
  .mapHeightToggle .mapHeightToggleIcon {
    top: 5px;
    left: 8px;
  }
}
.mobileControlToggle {
  line-height: 1em;
  outline: none;
  display: inline-block;
  border: 0;
  margin-right: 16px;
  padding: 0;
  user-select: none;
  width: 40px;
  height: 40px;
  border-radius: 20px;
  background-color: #333333;
  color: white;
  font-size: 24px;
  box-shadow: rgba(0, 0, 0, 0.3) 0 1px 4px -1px;
  fill: white;
  stroke: white;
  margin-bottom: 16px;
}
@media (min-width: 669px) {
  .lapDeskFontS {
    font-size: 1.3rem !important;
  }
}
.tooltip-container {
  width: 24px;
  height: 25px;
}
.tooltip-container .white-tooltip {
  width: 300px;
  background-color: #fff;
  color: #333333;
  box-shadow: 1px 1px 10px 10px rgba(0, 0, 0, 0.1);
}
.tooltip-container .white-tooltip.positioning-right:after {
  border-color: #fff transparent transparent #fff;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.modalOverlayBackground {
  padding: 30px 0;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(44, 44, 44, 0.75);
  z-index: 11730002;
  overflow: auto;
}
@media (max-width: 668px) {
  .modalOverlayBackground {
    padding: 0;
  }
}
.modalOverlayContentBox {
  background: #fff;
  min-width: 400px;
  max-width: 760px;
  margin: 0 auto;
  position: relative;
}
@media (min-width: 669px) {
  .modalOverlayContentBox.noiseOverlay {
    width: 620px;
    position: absolute;
    top: 50% !important;
    left: 50% !important;
    -webkit-transform: translateX(-50%) translateY(-50%);
    -moz-transform: translateX(-50%) translateY(-50%);
    -ms-transform: translateX(-50%) translateY(-50%);
    -o-transform: translateX(-50%) translateY(-50%);
    transform: translateX(-50%) translateY(-50%);
  }
}
@media (max-width: 668px) {
  .modalOverlayContentBox {
    min-width: initial;
    margin: 0;
    min-height: 100%;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.bubbleLegendMaximizedContainer {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  box-shadow: 1px 1px 40px rgba(0, 0, 0, 0.08);
  border-radius: 8px;
  padding: 16px 11px 16px 16px;
  background-color: #fff;
  margin-top: 12px;
  font-size: 14px;
  line-height: 22px;
  height: 188px;
  width: 298px;
}
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__colorCircle {
  width: 14px;
  height: 14px;
  opacity: 0.6;
  border-radius: 7px;
  margin-right: 4px;
  position: relative;
  top: 2px;
}
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__colorCircleEmpty {
  width: 14px;
  height: 14px;
  border: 1px solid #ADADAD;
  background-color: #fff;
  border-radius: 7px;
  margin-right: 4px;
  position: relative;
  top: 2px;
}
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__buttonContainer {
  top: 10px;
  right: 8px;
  height: 20px;
  width: 20px;
}
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__buttonContainer button {
  width: 20px;
  height: 20px;
}
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__buttonContainer button,
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__buttonContainer button:hover,
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__buttonContainer button:active,
.bubbleLegendMaximizedContainer .bubbleLegendMaximizedContainer__buttonContainer button:focus {
  color: #333333;
  text-decoration: none;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.bubbleLegendMinimizedContainer {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  box-shadow: 1px 1px 40px rgba(0, 0, 0, 0.08);
  border-radius: 8px;
  padding-left: 8px;
  background-color: #fff;
  margin-top: 12px;
  font-size: 14px;
  line-height: 22px;
  height: 40px;
  width: 298px;
}
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__colorBlockContainer {
  height: 16px;
}
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__colorBlockContainer .bubbleLegendMinimizedContainer__colorBlock {
  margin-right: 4px;
  opacity: 0.6;
  width: 7px;
  height: 16px;
}
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__colorBlockContainer .bubbleLegendMinimizedContainer__colorBlock:last-child {
  margin-right: 0;
}
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__buttonContainer {
  top: 10px;
  right: 8px;
  height: 20px;
  width: 20px;
}
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__buttonContainer button {
  width: 20px;
  height: 20px;
}
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__buttonContainer button,
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__buttonContainer button:hover,
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__buttonContainer button:active,
.bubbleLegendMinimizedContainer .bubbleLegendMinimizedContainer__buttonContainer button:focus {
  color: #333333;
  text-decoration: none;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.horizontalCenteredBubbleLegend {
  left: 50% !important;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.horizontalCenteredBubbleLegend {
  left: 50% !important;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
}
.gradientBubbleLegendContainer {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  box-shadow: 1px 1px 40px rgba(0, 0, 0, 0.08);
  padding: 6px 12px;
  background-color: #fff;
  font-size: 12px;
  line-height: 16px;
  height: 44px;
  width: 320px;
  max-width: calc(100vw - 24px);
}
.gradientBubbleLegendContainer .gradientBubbleLegendContainer_gradientCell {
  width: 100%;
  padding: 0 12px;
  height: 16px;
}
.gradientBubbleLegendContainer .gradientBubbleLegendContainer_gradientCell .gradientBubbleLegendContainer_gradient {
  height: 16px;
  width: 100%;
  border-radius: 4px;
}
.gradientBubbleLegendContainer.legend_style_classic {
  border-radius: 8px;
  margin-top: 12px;
}
.gradientBubbleLegendContainer.legend_style_new {
  border-radius: 22px;
  bottom: 68px;
  position: relative;
  transition: all 800ms cubic-bezier(0.84, 0.02, 0.37, 1.15);
  right: 0;
}
.gradientBubbleLegendContainer.legend_style_new.rightAligned {
  width: 80px;
  right: calc(-50vw + 10px);
}
.gradientBubbleLegendContainer.legend_style_new .minimizedLegendContainer .minimizedLegend {
  width: 24px;
  height: 24px;
  border-radius: 12px;
  background: linear-gradient(90deg, #00d9b1 0%, #f9d43a 50%, #dd0000 100%);
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.tooltipContainer {
  position: relative;
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  box-shadow: 0px 1px 3px 0px rgba(0, 0, 0, 0.35);
}
.tooltipContainer[data-anchorstyle="left"] {
  margin-left: 10px;
}
.tooltipContainer[data-anchorstyle="right"] {
  margin-right: 10px;
}
.tooltipContainer[data-anchorstyle="top_left"] {
  margin-top: 10px;
  margin-left: -25px;
}
.tooltipContainer[data-anchorstyle="top_right"] {
  margin-top: 10px;
  margin-right: -25px;
}
.tooltipContainer[data-anchorstyle="bottom_left"] {
  bottom: 10px;
  margin-left: -25px;
}
.tooltipContainer[data-anchorstyle="bottom_right"] {
  bottom: 10px;
  margin-right: -25px;
}
.tooltipContainer .tooltipContainer__content {
  border-radius: 4px;
  background-color: #ffffff;
  padding: 3px 8px;
  position: relative;
}
.tooltipContainer .tooltipContainer__price {
  font-size: 14px;
  line-height: 22px;
  font-weight: bold;
  color: #333333;
}
.tooltipContainer .tooltipContainer__location {
  font-size: 12px;
  line-height: 16px;
  color: #757575;
}
.tooltipContainer .tooltipContainer__arrow {
  position: absolute;
  z-index: 1;
  width: 10px;
  height: 10px;
  background-color: #ffffff;
}
.tooltipContainer .tooltipContainer__arrow[data-anchorstyle="left"] {
  left: 0px;
  top: 50%;
  -webkit-transform: translateX(-50%) translateY(-50%) rotate(45deg);
  -moz-transform: translateX(-50%) translateY(-50%) rotate(45deg);
  -ms-transform: translateX(-50%) translateY(-50%) rotate(45deg);
  -o-transform: translateX(-50%) translateY(-50%) rotate(45deg);
  transform: translateX(-50%) translateY(-50%) rotate(45deg);
}
.tooltipContainer .tooltipContainer__arrow[data-anchorstyle="right"] {
  right: 0px;
  top: 50%;
  -webkit-transform: translateX(50%) translateY(-50%) rotate(45deg);
  -moz-transform: translateX(50%) translateY(-50%) rotate(45deg);
  -ms-transform: translateX(50%) translateY(-50%) rotate(45deg);
  -o-transform: translateX(50%) translateY(-50%) rotate(45deg);
  transform: translateX(50%) translateY(-50%) rotate(45deg);
}
.tooltipContainer .tooltipContainer__arrow[data-anchorstyle="top_left"] {
  top: 0px;
  left: 20px;
  -webkit-transform: translateY(-50%) rotate(45deg);
  -moz-transform: translateY(-50%) rotate(45deg);
  -ms-transform: translateY(-50%) rotate(45deg);
  -o-transform: translateY(-50%) rotate(45deg);
  transform: translateY(-50%) rotate(45deg);
}
.tooltipContainer .tooltipContainer__arrow[data-anchorstyle="top_right"] {
  top: 0px;
  right: 20px;
  -webkit-transform: translateY(-50%) rotate(45deg);
  -moz-transform: translateY(-50%) rotate(45deg);
  -ms-transform: translateY(-50%) rotate(45deg);
  -o-transform: translateY(-50%) rotate(45deg);
  transform: translateY(-50%) rotate(45deg);
}
.tooltipContainer .tooltipContainer__arrow[data-anchorstyle="bottom_left"] {
  bottom: 0px;
  left: 20px;
  -webkit-transform: translateY(50%) rotate(45deg);
  -moz-transform: translateY(50%) rotate(45deg);
  -ms-transform: translateY(50%) rotate(45deg);
  -o-transform: translateY(50%) rotate(45deg);
  transform: translateY(50%) rotate(45deg);
}
.tooltipContainer .tooltipContainer__arrow[data-anchorstyle="bottom_right"] {
  bottom: 0px;
  right: 20px;
  -webkit-transform: translateY(50%) rotate(45deg);
  -moz-transform: translateY(50%) rotate(45deg);
  -ms-transform: translateY(50%) rotate(45deg);
  -o-transform: translateY(50%) rotate(45deg);
  transform: translateY(50%) rotate(45deg);
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.horizontalCenteredBubbleLegend {
  left: 50% !important;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
}
.bubbleLegendContainer {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  box-shadow: 1px 1px 40px rgba(0, 0, 0, 0.08);
  padding: 8px 12px;
  background-color: #fff;
  font-size: 12px;
  font-weight: 700;
  line-height: 16px;
  width: 238px;
  max-width: calc(100vw - 24px);
}
.bubbleLegendContainer .bubbleLegendContainer_containerColors {
  width: 68px;
  max-width: 68px;
  height: 16px;
  display: flex;
  justify-content: space-between;
}
.bubbleLegendContainer .bubbleLegendContainer_color {
  opacity: 0.6;
  width: 8px;
  max-width: 8px;
  height: 16px;
}
.bubbleLegendContainer .bubbleLegendContainer_color:first-child {
  border-bottom-left-radius: 5px;
  border-top-left-radius: 5px;
}
.bubbleLegendContainer .bubbleLegendContainer_color:last-child {
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  margin-right: 0;
}
.bubbleLegendContainer.legend_style_classic {
  border-radius: 8px;
  margin-top: 12px;
}
.bubbleLegendContainer.legend_style_new {
  border-radius: 8px;
  bottom: 68px;
  position: relative;
  transition: all 800ms cubic-bezier(0.84, 0.02, 0.37, 1.15);
  right: 0;
}
.bubbleLegendContainer.legend_style_new.rightAligned {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  padding: 8px;
  right: calc(-50vw + 40px);
}
.bubbleLegendContainer.legend_style_new .minimizedLegendContainer .minimizedLegend {
  border-radius: 8px;
  display: flex;
}
.bubbleLegendContainer.legend_style_new .minimizedLegendContainer .minimizedColorBlock {
  opacity: 0.6;
  width: 25%;
  height: 16px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.colorbox {
  font-size: 10px;
  height: 16px;
  text-align: center;
  width: 16px;
  display: inline-block;
  vertical-align: top;
  border-radius: 8px;
  margin-top: 2px;
  margin-left: 8px;
}
.namebox {
  margin-left: 8px;
}
.box16mbit {
  background-color: #FFDE5D;
  opacity: 0.5;
}
.box50mbit {
  background-color: #FFB356;
  opacity: 0.5;
}
.box100mbit {
  background-color: #E20074;
  opacity: 0.3;
}
.box250mbit {
  background-color: #E20074;
  opacity: 0.6;
}
.box1000mbit {
  background-color: #9d4e75;
  opacity: 0.6;
}
.boxhybrid {
  border: 1px solid #9e0050;
  background: url('//www.static-immobilienscout24.de/statpic/expose/icons/0d5b55b7e8b8f3fd0af21637602fb4c5_boxhybrid-v2-1x.png') no-repeat;
  background-size: contain;
}
.boxv50mbit {
  background-color: #529AD6;
  opacity: 0.5;
}
.boxv100mbit {
  background-color: #235482;
  opacity: 0.5;
}
.box260k {
  background-color: #FFB356;
  opacity: 0.5;
}
.box300m {
  background-color: #E20074;
  opacity: 0.3;
}
.box1g {
  background-color: #E20074;
  opacity: 0.6;
}
.telekomLegalNote i {
  color: black;
}
.telekomLink {
  color: #2a7cca;
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
}
.moreInfos {
  display: block;
  text-align: left;
  background: none;
  border: none;
  padding: 0;
  font-weight: 400 !important;
}
.moreInfos:hover {
  cursor: pointer;
}
.moreInfos:hover div {
  text-decoration: underline;
}
.verticalCentered {
  position: absolute;
  top: 50% !important;
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  transform: translateY(-50%);
}
.entry {
  margin-bottom: 0;
}
@media (min-width: 669px) {
  .entry {
    margin-bottom: 8px;
  }
}
.normalResolutionLogo {
  display: inline;
}
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .normalResolutionLogo {
    display: none;
  }
}
.highResolutionLogo {
  display: none;
}
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .highResolutionLogo {
    display: inline;
  }
}
button {
  background: none;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.blueDotIcon {
  display: block;
  cursor: pointer;
  height: 16px;
  width: 16px;
  position: relative;
  border-radius: 8px;
  background: #333333;
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.24);
}
.blueDotIcon .blueDotIconInnerTeal {
  border-radius: 6px;
  position: absolute;
  left: 2px;
  top: 2px;
  height: 12px;
  width: 12px;
  background: #00ffd0;
}
.blueDotIcon:hover {
  z-index: 101;
}
.blueDotIcon:hover .blueDotIconInnerTeal {
  background: #00d9b1;
}
.blackDotIcon {
  display: block;
  cursor: pointer;
  height: 16px;
  width: 16px;
  position: relative;
  border-radius: 8px;
  background: #ffffff;
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.24);
}
.blackDotIcon .blackDotIconInner {
  border-radius: 6px;
  position: absolute;
  left: 2px;
  top: 2px;
  height: 12px;
  width: 12px;
  background: #333333;
}
.blackDotIcon:hover {
  z-index: 101;
}
.blackDotIcon:hover .blackDotIconInner {
  background: #676767;
}
.styledMarkerContainer {
  padding-bottom: 5px;
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  font-size: 1.4rem;
  font-weight: 400;
  letter-spacing: 0.5px;
}
.styledMarkerWithoutAddress,
.styledMarker {
  position: relative;
  border-radius: 4px;
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.24);
  padding: 2px 9px;
  color: white;
  white-space: nowrap;
  background-color: #333333;
  cursor: pointer;
}
.styledMarkerWithoutAddress:hover,
.styledMarker:hover {
  background-color: #676767;
  box-shadow: 0px 4px 10px 2px rgba(0, 0, 0, 0.08);
  z-index: 101;
}
.styledMarkerWithoutAddress.active,
.styledMarker.active {
  background-color: #00ffd0;
  color: #333333;
  z-index: 100;
}
.styledMarker:after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  width: 0;
  height: 0;
  border-top: solid 5px #333333;
  border-left: solid 5px transparent;
  border-right: solid 5px transparent;
}
.styledMarker:hover:after {
  border-top: solid 5px #676767;
}
.styledMarker.active:after {
  border-top-color: #00ffd0;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.wheelmapLegendContainer img {
  height: 20px;
}
.wheelmapLegendContainer .copyRightContainer img {
  height: 24px;
}
.bottomBox {
  position: fixed;
  bottom: 0;
  right: 0;
}
.wheelmapAddress {
  color: #969696;
}
.wheelmapBottomSeparator {
  border-bottom: 1px #e0e0e0 solid;
  margin-bottom: 8px;
  padding-bottom: 8px;
}
.wheelmapCalloutTopic {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.zoomLevelMessageBox {
  position: absolute;
  z-index: 31;
  top: 50% !important;
  left: 50% !important;
  -webkit-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -ms-transform: translateX(-50%) translateY(-50%);
  -o-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}
.zoomLevelMessageBox .zoomLevelMessageBoxContent {
  width: 290px;
  padding: 16px;
}
.zoomLevelMessageBox .zoomLevelMessageBoxContent .zoomLevelMessageBoxMainText {
  padding-left: 24px;
  padding-right: 24px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.mapCallout {
  position: absolute;
  bottom: 0;
  left: 50%;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  line-height: 1.61;
  padding: 10px;
}
@media (max-width: 668px) {
  .mapCallout {
    max-width: 370px;
  }
}
@media (min-width: 669px) {
  .mapCallout {
    width: 618px;
    max-width: 628px;
  }
}
.mapCallout .mapCalloutContent {
  box-shadow: 1px 1px 2px 0 rgba(0, 0, 0, 0.5);
}
.mapCallout .criteriaContainer {
  float: left;
  width: 57%;
}
.mapCallout .virtualPlaceholder {
  padding-top: 75%;
}
.mapCallout .calloutOptions {
  height: 40px;
  bottom: 0;
  right: 0;
  left: 43%;
  background-color: #f2f2f2;
}
@media (min-width: 669px) {
  .mapCallout .calloutOptions {
    position: absolute;
  }
}
@media (max-width: 668px) {
  .mapCallout .calloutOptions {
    width: 100%;
  }
}
.mapCallout .optionButton {
  width: 40px;
  height: 100%;
  color: #757575;
}
.mapCallout .optionButton:hover {
  color: #333333;
}
.mapCallout .optionButton i {
  margin-top: 3px;
  margin-left: 3px;
}
@media (max-width: 668px) {
  .mapCallout .optionButton i {
    margin-left: 5px;
  }
}
@media (min-width: 669px) {
  .mapCallout .attributes {
    font-size: 1.8rem;
    height: 34px;
  }
}
@media (max-width: 668px) {
  .mapCallout .attributes {
    font-size: 2rem;
  }
}
@media (min-width: 669px) {
  .mapCallout .withBorder {
    border-right: 1px solid #e0e0e0;
  }
}
.mapCallout .pagingContainer {
  min-height: 1em;
  display: inline-table;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -100%);
  white-space: nowrap;
}
.mapCallout .closeButton {
  position: absolute;
  -webkit-transform: translateY(-100%);
  -moz-transform: translateY(-100%);
  -ms-transform: translateY(-100%);
  -o-transform: translateY(-100%);
  transform: translateY(-100%);
  right: 0;
  top: 0;
}
.mapCallout .pagingText {
  padding: 8px 16px 6px;
  height: 36px;
}
@media (min-width: 360px) {
  .mapCallout .pagingText .pagingTextShort {
    display: none;
  }
}
@media (max-width: 359px) {
  .mapCallout .pagingText .pagingTextNormal {
    display: none;
  }
}
.mapCallout .pagingButton {
  padding: 4px 16px;
  font-size: 2rem;
  border: 0;
  color: #343434;
  height: 36px;
}
@media (min-width: 669px) {
  .mapCallout .pagingButton {
    font-size: 2rem;
  }
}
.mapCallout .pagingButtonLeft {
  padding: 4px 16px;
  font-size: 2rem;
  border: 0;
  color: #343434;
  height: 36px;
  border-right: 1px solid #e0e0e0;
  border-top-left-radius: 15px;
  -moz-border-top-left-radius: 15px;
}
@media (min-width: 669px) {
  .mapCallout .pagingButtonLeft {
    font-size: 2rem;
  }
}
.mapCallout .pagingButtonRight {
  padding: 4px 16px;
  font-size: 2rem;
  border: 0;
  color: #343434;
  height: 36px;
  border-left: 1px solid #e0e0e0;
  border-top-right-radius: 15px;
  -moz-border-top-right-radius: 15px;
}
@media (min-width: 669px) {
  .mapCallout .pagingButtonRight {
    font-size: 2rem;
  }
}
.mapCallout .pagingButtonLeft:disabled,
.mapCallout .pagingButtonRight:disabled {
  color: #969696;
}
.maxtwoliner-basic {
  white-space: normal;
  word-break: normal;
  overflow: hidden;
  display: block;
  text-overflow: ellipsis;
}
.maxtwoliner {
  white-space: normal;
  word-break: normal;
  overflow: hidden;
  display: block;
  text-overflow: ellipsis;
  max-height: 3.22em;
}
.maxtwolinerHeadline {
  white-space: normal;
  word-break: normal;
  overflow: hidden;
  display: block;
  text-overflow: ellipsis;
  max-height: 2.66em;
  line-height: 1.33 !important;
}
.maxtwoliner,
.maxtwoliner * {
  line-height: 1.61 !important;
}
.sublist .maxtwoliner {
  max-height: 2.8em;
}
.linkHeadlineColor {
  color: #333333 !important;
}
.shortlistButton:hover {
  color: #ff7070 !important;
}
.shortlistButton .active {
  color: #ff7070;
}
.calloutContentMessage {
  border: 1px solid #e0e0e0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 156px;
}
@media (min-width: 669px) {
  .calloutContentMessage {
    height: 194px;
  }
}
.mapCalloutAddress {
  color: #646464;
}
.mapCalloutAddress .mapCalloutAddressIcon {
  position: relative;
  top: 2px;
}
.mapCalloutAddress .mapCalloutAddressText {
  margin-left: 4px;
}
.popupMenuContainer {
  position: absolute;
  right: -8px;
  bottom: 37px;
  padding: 8px;
  box-shadow: 0 0 8px 4px rgba(0, 0, 0, 0.2);
  z-index: 1;
}
.popupMenuContainer .popupLink {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  color: #333333;
  margin: 8px;
}
.popupMenuContainer .popupLink:hover {
  color: #333333;
  text-decoration: underline;
}
.popupMenuContainer .popupLink .iconContainer {
  width: 14px;
  height: 0.7em;
  display: inline-block;
  position: relative;
  margin-right: 3px;
}
.popupMenuContainer .popupLink .iconContainer .iconSymbol {
  position: absolute;
  left: 50% !important;
  top: 50% !important;
  -webkit-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -ms-transform: translateX(-50%) translateY(-50%);
  -o-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}
.popupMenuContainer .popupLink .iconContainer .iconSymbol.active {
  color: #ff7070;
}
.callout-lfl {
  background-color: #333333 !important;
  color: #e0e0e0;
}
.callout-lfl .lfl-bottom-container {
  height: 40px;
  bottom: 0;
  right: 0;
}
.callout-lfl .border-top {
  border-color: #676767;
}
.callout-lfl .mapCalloutAddress {
  color: #e0e0e0;
}
.callout-lfl .linkHeadlineColor {
  color: #e0e0e0 !important;
}
.callout-lfl .optionButton {
  color: #fff;
}
.callout-lfl .optionButton:hover {
  color: #fff;
}
.callout-lfl .mainCriteria {
  color: #fff;
}
.fontColorLfl {
  color: #e0e0e0 !important;
}
.vertical-highlighter {
  display: inline-block;
  background: url("https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/priority-line-vertical.svg") no-repeat;
  width: 8px;
  height: 24px;
}
.underline-highlighter-kplus {
  position: relative;
}
.underline-highlighter-kplus::before {
  content: "";
  background: url(https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/underline-kplus.svg) no-repeat;
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 21px;
  height: 4px;
}
.plus-highlighter {
  position: relative;
  margin-right: 8px;
}
.plus-highlighter::after {
  content: "";
  background: url(https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/kplus-teal-icon.svg) no-repeat;
  position: absolute;
  top: -1px;
  left: 90%;
  width: 11px;
  height: 10px;
}
.with-icon {
  color: #fff;
}
.lfl-info {
  background-color: #333333;
  padding-right: 0 !important;
}
.list-first-listing-vertical-line:before {
  position: absolute;
  bottom: 11px;
  left: 15px;
  width: 8px;
  height: 60%;
  background: url(https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/priority-line-vertical.svg) 0 0 no-repeat;
  background-size: cover;
  content: '';
}
@media (max-width: 668px) {
  .list-first-listing-vertical-line:before {
    left: 16px;
    height: 72%;
  }
}
@media (min-width: 430px) and (max-width: 668px) {
  .list-first-listing-vertical-line:before {
    height: 60%;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.mapCallout {
  position: absolute;
  bottom: 0;
  left: 50%;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  line-height: 1.61;
  padding: 10px;
}
@media (max-width: 668px) {
  .mapCallout {
    max-width: 370px;
  }
}
@media (min-width: 669px) {
  .mapCallout {
    width: 618px;
    max-width: 628px;
  }
}
.mapCallout .mapCalloutContent {
  box-shadow: 1px 1px 2px 0 rgba(0, 0, 0, 0.5);
}
.mapCallout .criteriaContainer {
  float: left;
  width: 57%;
}
.mapCallout .virtualPlaceholder {
  padding-top: 75%;
}
.mapCallout .calloutOptions {
  height: 40px;
  bottom: 0;
  right: 0;
  left: 43%;
  background-color: #f2f2f2;
}
@media (min-width: 669px) {
  .mapCallout .calloutOptions {
    position: absolute;
  }
}
@media (max-width: 668px) {
  .mapCallout .calloutOptions {
    width: 100%;
  }
}
.mapCallout .optionButton {
  width: 40px;
  height: 100%;
  color: #757575;
}
.mapCallout .optionButton:hover {
  color: #333333;
}
.mapCallout .optionButton i {
  margin-top: 3px;
  margin-left: 3px;
}
@media (max-width: 668px) {
  .mapCallout .optionButton i {
    margin-left: 5px;
  }
}
@media (min-width: 669px) {
  .mapCallout .attributes {
    font-size: 1.8rem;
    height: 34px;
  }
}
@media (max-width: 668px) {
  .mapCallout .attributes {
    font-size: 2rem;
  }
}
@media (min-width: 669px) {
  .mapCallout .withBorder {
    border-right: 1px solid #e0e0e0;
  }
}
.mapCallout .pagingContainer {
  min-height: 1em;
  display: inline-table;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -100%);
  white-space: nowrap;
}
.mapCallout .closeButton {
  position: absolute;
  -webkit-transform: translateY(-100%);
  -moz-transform: translateY(-100%);
  -ms-transform: translateY(-100%);
  -o-transform: translateY(-100%);
  transform: translateY(-100%);
  right: 0;
  top: 0;
}
.mapCallout .pagingText {
  padding: 8px 16px 6px;
  height: 36px;
}
@media (min-width: 360px) {
  .mapCallout .pagingText .pagingTextShort {
    display: none;
  }
}
@media (max-width: 359px) {
  .mapCallout .pagingText .pagingTextNormal {
    display: none;
  }
}
.mapCallout .pagingButton {
  padding: 4px 16px;
  font-size: 2rem;
  border: 0;
  color: #343434;
  height: 36px;
}
@media (min-width: 669px) {
  .mapCallout .pagingButton {
    font-size: 2rem;
  }
}
.mapCallout .pagingButtonLeft {
  padding: 4px 16px;
  font-size: 2rem;
  border: 0;
  color: #343434;
  height: 36px;
  border-right: 1px solid #e0e0e0;
  border-top-left-radius: 15px;
  -moz-border-top-left-radius: 15px;
}
@media (min-width: 669px) {
  .mapCallout .pagingButtonLeft {
    font-size: 2rem;
  }
}
.mapCallout .pagingButtonRight {
  padding: 4px 16px;
  font-size: 2rem;
  border: 0;
  color: #343434;
  height: 36px;
  border-left: 1px solid #e0e0e0;
  border-top-right-radius: 15px;
  -moz-border-top-right-radius: 15px;
}
@media (min-width: 669px) {
  .mapCallout .pagingButtonRight {
    font-size: 2rem;
  }
}
.mapCallout .pagingButtonLeft:disabled,
.mapCallout .pagingButtonRight:disabled {
  color: #969696;
}
.maxtwoliner-basic {
  white-space: normal;
  word-break: normal;
  overflow: hidden;
  display: block;
  text-overflow: ellipsis;
}
.maxtwoliner {
  white-space: normal;
  word-break: normal;
  overflow: hidden;
  display: block;
  text-overflow: ellipsis;
  max-height: 3.22em;
}
.maxtwolinerHeadline {
  white-space: normal;
  word-break: normal;
  overflow: hidden;
  display: block;
  text-overflow: ellipsis;
  max-height: 2.66em;
  line-height: 1.33 !important;
}
.maxtwoliner,
.maxtwoliner * {
  line-height: 1.61 !important;
}
.sublist .maxtwoliner {
  max-height: 2.8em;
}
.linkHeadlineColor {
  color: #333333 !important;
}
.shortlistButton:hover {
  color: #ff7070 !important;
}
.shortlistButton .active {
  color: #ff7070;
}
.calloutContentMessage {
  border: 1px solid #e0e0e0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 156px;
}
@media (min-width: 669px) {
  .calloutContentMessage {
    height: 194px;
  }
}
.mapCalloutAddress {
  color: #646464;
}
.mapCalloutAddress .mapCalloutAddressIcon {
  position: relative;
  top: 2px;
}
.mapCalloutAddress .mapCalloutAddressText {
  margin-left: 4px;
}
.popupMenuContainer {
  position: absolute;
  right: -8px;
  bottom: 37px;
  padding: 8px;
  box-shadow: 0 0 8px 4px rgba(0, 0, 0, 0.2);
  z-index: 1;
}
.popupMenuContainer .popupLink {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  color: #333333;
  margin: 8px;
}
.popupMenuContainer .popupLink:hover {
  color: #333333;
  text-decoration: underline;
}
.popupMenuContainer .popupLink .iconContainer {
  width: 14px;
  height: 0.7em;
  display: inline-block;
  position: relative;
  margin-right: 3px;
}
.popupMenuContainer .popupLink .iconContainer .iconSymbol {
  position: absolute;
  left: 50% !important;
  top: 50% !important;
  -webkit-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -ms-transform: translateX(-50%) translateY(-50%);
  -o-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}
.popupMenuContainer .popupLink .iconContainer .iconSymbol.active {
  color: #ff7070;
}
.callout-lfl {
  background-color: #333333 !important;
  color: #e0e0e0;
}
.callout-lfl .lfl-bottom-container {
  height: 40px;
  bottom: 0;
  right: 0;
}
.callout-lfl .border-top {
  border-color: #676767;
}
.callout-lfl .mapCalloutAddress {
  color: #e0e0e0;
}
.callout-lfl .linkHeadlineColor {
  color: #e0e0e0 !important;
}
.callout-lfl .optionButton {
  color: #fff;
}
.callout-lfl .optionButton:hover {
  color: #fff;
}
.callout-lfl .mainCriteria {
  color: #fff;
}
.fontColorLfl {
  color: #e0e0e0 !important;
}
.vertical-highlighter {
  display: inline-block;
  background: url("https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/priority-line-vertical.svg") no-repeat;
  width: 8px;
  height: 24px;
}
.underline-highlighter-kplus {
  position: relative;
}
.underline-highlighter-kplus::before {
  content: "";
  background: url(https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/underline-kplus.svg) no-repeat;
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 21px;
  height: 4px;
}
.plus-highlighter {
  position: relative;
  margin-right: 8px;
}
.plus-highlighter::after {
  content: "";
  background: url(https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/kplus-teal-icon.svg) no-repeat;
  position: absolute;
  top: -1px;
  left: 90%;
  width: 11px;
  height: 10px;
}
.with-icon {
  color: #fff;
}
.lfl-info {
  background-color: #333333;
  padding-right: 0 !important;
}
.list-first-listing-vertical-line:before {
  position: absolute;
  bottom: 11px;
  left: 15px;
  width: 8px;
  height: 60%;
  background: url(https://www.static-immobilienscout24.de/fro/is24-cxp-map/icons/priority-line-vertical.svg) 0 0 no-repeat;
  background-size: cover;
  content: '';
}
@media (max-width: 668px) {
  .list-first-listing-vertical-line:before {
    left: 16px;
    height: 72%;
  }
}
@media (min-width: 430px) and (max-width: 668px) {
  .list-first-listing-vertical-line:before {
    height: 60%;
  }
}
.galleryContainer {
  float: left;
  width: 43% !important;
}
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .galleryContainer .virtual-tour-icon {
    background-size: 72px 72px;
    background-image: url("https://www.static-immobilienscout24.de/statpic/expose/gallery/f076cfbabc24d0c4a7b16c0209680385_icn_360__72x72.png");
  }
}
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .galleryContainer .video-play-icon {
    background-size: 72px 72px;
    background-image: url("https://www.static-immobilienscout24.de/statpic/expose/gallery/e255c8d8ef0f54cb3ec0fac471804352_icn_video__72x72@2x.png");
  }
}
.galleryContainer .virtual-tour-icon {
  background-image: url("https://www.static-immobilienscout24.de/statpic/expose/gallery/f076cfbabc24d0c4a7b16c0209680385_icn_360__72x72.png");
  background-size: 72px 72px;
}
.galleryContainer .virtual-tour-icon,
.galleryContainer .video-play-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -ms-transform: translateX(-50%) translateY(-50%);
  -o-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
  height: 72px;
  width: 72px;
}
.galleryContainer .video-play-icon {
  background-image: url("https://www.static-immobilienscout24.de/statpic/expose/gallery/e3c5d0fa38cb013f1bf367dfda3c6286_icn_video__72x72.png");
  background-size: 72px 72px;
}
.galleryContainer .video-image {
  max-height: 100%;
  max-width: 100%;
  margin: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
.imageContainer {
  top: 0;
  left: 0;
  position: absolute;
  height: 100%;
  width: 100%;
  background-color: #e0e0e0;
}
.imageContainer .slick-prev {
  left: 0;
}
.imageContainer .slick-next {
  right: 0;
}
.imageContainer .slick-arrow {
  color: #fff;
  font-weight: 100;
  font-size: 40px;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
  cursor: pointer;
  filter: drop-shadow(0px 2px 4px rgba(0, 0, 0, 0.5));
  border: none;
}
@media (max-width: 668px) {
  .imageContainer .slick-arrow {
    font-size: 32px;
  }
}
.galleryImage {
  display: block;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  max-height: 100%;
  position: absolute;
}
.galleryImage[data-listing-type='M'],
.galleryImage[data-listing-type='S'] {
  padding: 10%;
}
.virtualPlaceholder {
  padding-top: 75%;
}
.galleryCountContainer {
  bottom: 8px;
  left: 8px;
  position: absolute;
  background-color: #646464;
  color: #fff;
  padding: 4px 6px;
}
.listFirstGalleryCountContainer {
  bottom: 8px;
  left: 8px;
  position: absolute;
  background-color: #EAEAEA;
  color: #333333;
  padding: 4px 6px;
  border-radius: 4px;
}
.galleryNoPictureContainer {
  width: 100%;
  height: 100%;
  background-color: #e0e0e0;
  color: #757575;
}
.galleryNoPictureContainer .galleryNoPicture {
  background: url("https://www.static-immobilienscout24.de/statpic/d3f18e7fdcf061fc7cb116df6beade2c_no-picture-placeholder-optimized.svg") no-repeat center;
  background-size: contain;
  height: 80px;
  width: 130px;
}
@media (max-width: 668px) {
  .galleryNoPictureContainer .galleryNoPicture {
    height: 40px;
  }
}
.icon-align-center.is24-icon-chevron-right::before {
  vertical-align: -9%;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
@media (max-width: 668px) {
  .lfl-modal-container {
    height: 100%;
  }
}
.lfl-modal-container .lfl-modal-description .list-check li {
  margin-top: 8px;
  margin-bottom: 8px;
}
.lfl-info-container {
  position: relative;
  width: 30px;
  height: 20px;
  vertical-align: middle;
  overflow: visible;
  display: inline-block;
  font-size: 1.4rem;
  padding-left: 4px;
}
@media (min-width: 669px) {
  .lfl-info-container {
    padding-left: 4px;
  }
}
.lfl-info-container .is24-icon-info {
  cursor: pointer;
}
body.prevent-scroll {
  overflow: hidden;
  height: 100vh;
}
</style><style type="text/css">.Modal_modal-backdrop__r1muI{background-color:rgba(0,0,0,.7);height:100vh;left:0;position:fixed;width:100%}@media (max-width:668px){.Modal_modal-backdrop__r1muI{bottom:0}}@media (min-width:669px){.Modal_modal-backdrop__r1muI{top:0}}.Modal_modal-container__tRxlB{background:#fff;position:relative}@media (max-width:668px){.Modal_modal-container__tRxlB{border-radius:4px 4px 0 0;bottom:0;position:absolute;width:inherit!important}}@media (min-width:669px){.Modal_modal-container__tRxlB{border-radius:4px;margin:auto;position:relative;top:50%;transform:translateY(-50%);vertical-align:middle}}.Modal_no-title-wrapper__mmXE-{padding-top:25px}.Modal_modal-title-wrapper__mF9HN{border-bottom:1px solid #eaeaea;max-height:112px;padding:24px 64px 24px 32px;text-align:left}.Modal_modal-close-button__ynL08{background-color:transparent;border:none;cursor:pointer;font-size:12px;padding-top:26px;position:absolute;right:0;top:0}@media (max-width:668px){.Modal_modal-close-button__ynL08{padding-right:18px}}@media (min-width:669px){.Modal_modal-close-button__ynL08{padding-right:34px}}.Modal_modal-headline__f7I77{font-weight:400;margin-bottom:0}.Modal_modal-content-wrapper__6U0AL{overflow:auto}@media (max-width:668px){.Modal_modal-content-wrapper__6U0AL{max-height:calc(100vh - 57px)}}@media (min-width:669px){.Modal_modal-content-wrapper__6U0AL{max-height:calc(100vh - 192px)}}.Modal_modal-content__sB2QR{display:block}@media (max-width:668px){.Modal_modal-content__sB2QR{padding:16px 24px}}@media (min-width:669px){.Modal_modal-content__sB2QR{padding:24px 32px}}</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.markerBubble {
  height: 64px;
  width: 64px;
  border-radius: 32px;
  background: #ffffff !important;
  border: 1px solid #ffffff;
  color: #2267e8;
  font-size: 11px;
  position: relative;
  cursor: pointer;
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  line-height: 1.61;
  outline: none;
}
.markerBubble:hover {
  color: #2267e8;
}
.markerBubble .markerBubbleText {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -ms-transform: translateX(-50%) translateY(-50%);
  -o-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
  text-align: center;
  text-decoration: none;
}
.markerBubble .markerBubbleText:hover {
  text-decoration: underline;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.cxpStatusMessageFeature {
  background-color: #fff;
  color: #4c4c4c;
  padding: 8px 16px;
  margin-top: 10px;
  margin-right: 6px;
  border-radius: 40px;
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
}
@media (max-width: 360px) {
  [data-theme="core"] .cxpStatusMessageFeature {
    margin-top: calc(var(--viewport-height) - var(--header-height) - 128px);
    margin-right: calc(100vw * 1/6);
  }
  [data-theme="cosma"] .cxpStatusMessageFeature {
    margin-top: calc(var(--viewport-height) - var(--header-height) - 150px);
    margin-right: calc(100vw * 1/6);
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.map-error-box-outer-container {
  z-index: 3000;
}
.map-error-box-outer-container .map-error-box-container {
  z-index: 3000;
  position: fixed;
  width: 100%;
  padding: 0;
  margin-top: 16px;
}
@media (max-width: 668px) {
  .map-error-box-outer-container .map-error-box-container {
    margin-top: 0;
  }
}
.map-error-box-outer-container .map-error-box-container .map-error-box-animation {
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  -webkit-animation-delay: 0.5s;
  animation-delay: 0.5s;
  -webkit-animation-name: mapErrorBoxfadeInDown;
  animation-name: mapErrorBoxfadeInDown;
}
.map-error-box-outer-container .map-error-box-container .map-error-box-animation .map-error-box {
  overflow: hidden;
  box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.33);
  padding-top: 16px;
  padding-bottom: 16px;
  min-height: 60px;
  width: 650px;
  margin: 0 auto 10px;
}
.map-error-box-outer-container .map-error-box-container .map-error-box-animation .map-error-box::before {
  padding: 100% 0;
  height: auto;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}
@media (max-width: 668px) {
  .map-error-box-outer-container .map-error-box-container .map-error-box-animation .map-error-box {
    width: 100%;
    margin-bottom: 0;
    box-shadow: 0 4px 2px -2px rgba(0, 0, 0, 0.33);
  }
  .map-error-box-outer-container .map-error-box-container .map-error-box-animation .map-error-box:not(:last-child) {
    box-shadow: none;
    border-bottom: 1px solid #fff;
  }
}
@-webkit-keyframes mapErrorBoxfadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translateY(-50px);
    transform: translateY(-50px);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
}
@keyframes mapErrorBoxfadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translateY(-50px);
    -ms-transform: translateY(-50px);
    transform: translateY(-50px);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateY(0);
    -ms-transform: translateY(0);
    transform: translateY(0);
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.objectSearchIntroductionContainer {
  position: absolute;
  width: 100%;
  height: 100%;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: rgba(0, 0, 0, 0.5);
  flex-direction: column;
}
.objectSearchIntroductionContainer .introText {
  width: 328px;
  font-size: 14px;
}
@media (max-height: 480px) {
  .objectSearchIntroductionContainer .introText {
    font-size: 12px;
  }
}
@media (min-width: 669px) {
  .objectSearchIntroductionContainer .introText {
    width: 480px;
    font-size: 18px;
  }
}
.objectSearchIntroductionContainer .introTitle {
  font-size: 20px;
  font-weight: 400;
}
@media (max-height: 480px) {
  .objectSearchIntroductionContainer .introTitle {
    font-size: 16px;
  }
}
@media (min-width: 669px) {
  .objectSearchIntroductionContainer .introTitle {
    font-size: 24px;
    font-weight: 700;
  }
}
.objectSearchIntroductionContainer .introImage {
  width: 140px;
  height: 140px;
  background-size: 140px;
  background-image: url("//www.static-immobilienscout24.de/statpic/cxp/map/aba780cd79629db497a516bbccdf89c9_object_introduction_overlay_map-mobile.png");
}
@media (max-height: 560px) {
  .objectSearchIntroductionContainer .introImage {
    width: 80px;
    height: 80px;
    background-size: 80px;
  }
}
@media (min-width: 669px) {
  .objectSearchIntroductionContainer .introImage {
    width: 180px;
    height: 180px;
    background-size: 180px;
    background-image: url("//www.static-immobilienscout24.de/statpic/cxp/map/1f6855ca605778818c767129cf6ced08_object_introduction_overlay_map-desktop.png");
  }
}
.objectSearchIntroductionContainer .introButton {
  width: 140px;
}
.objectSearchIntroductionContainer .introZoomControl {
  display: block;
  position: absolute;
  width: 40px;
  right: 10px;
  top: 70px;
  box-shadow: 0px 0px 10px 5px #fff;
  border-radius: 3px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.newCalloutEntry .imageWithNumberOfUnits {
  width: 43%;
  background-color: #EAEAEA;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
@media (max-width: 668px) {
  .newCalloutEntry .imageWithNumberOfUnits .image {
    height: 20px;
  }
}
.newCalloutEntry .imageWithNumberOfUnits .numberOfUnitsText {
  font-size: 12px;
  padding: 0 48px;
  margin-top: 14px;
}
@media (max-width: 668px) {
  .newCalloutEntry .imageWithNumberOfUnits .numberOfUnitsText {
    padding: 0;
    margin-top: 10px;
  }
}
.newCalloutEntry .objectDetails {
  width: 57%;
}
@media (max-width: 668px) {
  .newCalloutEntry .objectDetails {
    line-height: 16px;
  }
}
.newCalloutEntry .objectDetails .locationText {
  width: 280px;
  white-space: pre-wrap;
}
@media (max-width: 668px) {
  .newCalloutEntry .objectDetails .locationText {
    width: 150px;
    font-size: 12px;
    line-height: 16px;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.mapToggle__autoWidth {
  width: auto !important;
}
.mapToggle__newLabel {
  display: inline-flex;
  position: relative;
  width: 47px;
  top: 0;
}
@media (max-width: 668px) {
  .mapToggle__newLabel {
    width: 51px;
  }
}
@media (max-width: 353px) {
  .mapToggle__newLabel {
    display: none;
  }
}
.mapToggle__newLabel div {
  position: absolute;
  bottom: -7px;
  left: 0;
  background-repeat: no-repeat;
  background-size: cover;
  height: 24px;
  width: 43px;
  background-image: url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/b01c8387560a5ef0e0e9dfaa4aa0a8f4_Brand%20Label%20Teal.png");
  background-image: -webkit-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/b01c8387560a5ef0e0e9dfaa4aa0a8f4_Brand%20Label%20Teal.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/6a45602ec1269e10e8b497e1dbc492eb_Brand%20Label%20Teal@2x.png") 2x);
  background-image: -moz-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/b01c8387560a5ef0e0e9dfaa4aa0a8f4_Brand%20Label%20Teal.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/6a45602ec1269e10e8b497e1dbc492eb_Brand%20Label%20Teal@2x.png") 2x);
  background-image: -o-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/b01c8387560a5ef0e0e9dfaa4aa0a8f4_Brand%20Label%20Teal.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/6a45602ec1269e10e8b497e1dbc492eb_Brand%20Label%20Teal@2x.png") 2x);
  background-image: -ms-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/b01c8387560a5ef0e0e9dfaa4aa0a8f4_Brand%20Label%20Teal.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/6a45602ec1269e10e8b497e1dbc492eb_Brand%20Label%20Teal@2x.png") 2x);
}
@media (max-width: 668px) {
  .mapToggle__newLabel div {
    bottom: -12px;
  }
}
@media (min-width: 669px) {
  .button-primary .mapToggle__newLabel div {
    background-image: url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/1df25d6a100386e82062a77459689c00_Brand%20Label.png");
    background-image: -webkit-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/1df25d6a100386e82062a77459689c00_Brand%20Label.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/d6e35dc7aecb89ad4319ee77a7220aa6_Brand%20Label@2x.png") 2x);
    background-image: -moz-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/1df25d6a100386e82062a77459689c00_Brand%20Label.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/d6e35dc7aecb89ad4319ee77a7220aa6_Brand%20Label@2x.png") 2x);
    background-image: -o-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/1df25d6a100386e82062a77459689c00_Brand%20Label.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/d6e35dc7aecb89ad4319ee77a7220aa6_Brand%20Label@2x.png") 2x);
    background-image: -ms-image-set(url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/1df25d6a100386e82062a77459689c00_Brand%20Label.png") 1x, url("https://www.static-immobilienscout24.de/statpic/shared-services/it/search-web/icons/d6e35dc7aecb89ad4319ee77a7220aa6_Brand%20Label@2x.png") 2x);
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.searchHitButtonLoader {
  height: 18px;
  width: 18px;
  background-size: 18px;
}
</style><style type="text/css">.RadioButton_input-text-container__Xn5IM,.RadioButton_select-container__-qm8A,.RadioButton_textarea-container__iFSSB{position:relative}.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-left__szS9l,.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-right__A46fn,.RadioButton_input-text-container__Xn5IM>.RadioButton_input-icon-left__6IerX,.RadioButton_input-text-container__Xn5IM>.RadioButton_input-icon-right__Rx31T,.RadioButton_select-container__-qm8A>.RadioButton_affix-left__szS9l,.RadioButton_select-container__-qm8A>.RadioButton_affix-right__A46fn,.RadioButton_select-container__-qm8A>.RadioButton_input-icon-left__6IerX,.RadioButton_select-container__-qm8A>.RadioButton_input-icon-right__Rx31T,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-left__szS9l,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-right__A46fn,.RadioButton_textarea-container__iFSSB>.RadioButton_input-icon-left__6IerX,.RadioButton_textarea-container__iFSSB>.RadioButton_input-icon-right__Rx31T{color:#333;font-size:24px;line-height:40px;margin-left:12px;margin-right:12px;pointer-events:none;position:absolute;z-index:1}.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-left__szS9l+.RadioButton_select__YQgVe,.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-left__szS9l~.RadioButton_input-text__-vtHK,.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-right__A46fn+.RadioButton_select__YQgVe,.RadioButton_input-text-container__Xn5IM>.RadioButton_input-icon-left__6IerX+.RadioButton_select__YQgVe,.RadioButton_input-text-container__Xn5IM>.RadioButton_input-icon-left__6IerX~.RadioButton_input-text__-vtHK,.RadioButton_input-text-container__Xn5IM>.RadioButton_input-icon-right__Rx31T+.RadioButton_select__YQgVe,.RadioButton_select-container__-qm8A>.RadioButton_affix-left__szS9l+.RadioButton_select__YQgVe,.RadioButton_select-container__-qm8A>.RadioButton_affix-left__szS9l~.RadioButton_input-text__-vtHK,.RadioButton_select-container__-qm8A>.RadioButton_affix-right__A46fn+.RadioButton_select__YQgVe,.RadioButton_select-container__-qm8A>.RadioButton_input-icon-left__6IerX+.RadioButton_select__YQgVe,.RadioButton_select-container__-qm8A>.RadioButton_input-icon-left__6IerX~.RadioButton_input-text__-vtHK,.RadioButton_select-container__-qm8A>.RadioButton_input-icon-right__Rx31T+.RadioButton_select__YQgVe,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-left__szS9l+.RadioButton_select__YQgVe,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-left__szS9l~.RadioButton_input-text__-vtHK,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-right__A46fn+.RadioButton_select__YQgVe,.RadioButton_textarea-container__iFSSB>.RadioButton_input-icon-left__6IerX+.RadioButton_select__YQgVe,.RadioButton_textarea-container__iFSSB>.RadioButton_input-icon-left__6IerX~.RadioButton_input-text__-vtHK,.RadioButton_textarea-container__iFSSB>.RadioButton_input-icon-right__Rx31T+.RadioButton_select__YQgVe{padding-left:44px}.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-right__A46fn,.RadioButton_input-text-container__Xn5IM>.RadioButton_input-icon-right__Rx31T,.RadioButton_select-container__-qm8A>.RadioButton_affix-right__A46fn,.RadioButton_select-container__-qm8A>.RadioButton_input-icon-right__Rx31T,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-right__A46fn,.RadioButton_textarea-container__iFSSB>.RadioButton_input-icon-right__Rx31T{right:0}.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-right__A46fn~.RadioButton_input-text__-vtHK,.RadioButton_input-text-container__Xn5IM>.RadioButton_input-icon-right__Rx31T~.RadioButton_input-text__-vtHK,.RadioButton_select-container__-qm8A>.RadioButton_affix-right__A46fn~.RadioButton_input-text__-vtHK,.RadioButton_select-container__-qm8A>.RadioButton_input-icon-right__Rx31T~.RadioButton_input-text__-vtHK,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-right__A46fn~.RadioButton_input-text__-vtHK,.RadioButton_textarea-container__iFSSB>.RadioButton_input-icon-right__Rx31T~.RadioButton_input-text__-vtHK{padding-right:44px}.RadioButton_input-text-container__Xn5IM>.RadioButton_affix-unit__vQ6J0,.RadioButton_select-container__-qm8A>.RadioButton_affix-unit__vQ6J0,.RadioButton_textarea-container__iFSSB>.RadioButton_affix-unit__vQ6J0{font-size:16px;margin-left:auto;margin-right:auto;text-align:center;width:44px}.RadioButton_input-text__-vtHK,.RadioButton_select__YQgVe,.RadioButton_textarea__Nvz33{background-color:#fff;border:1px solid #adadad;border-radius:4px;caret-color:#333;color:#333;font-family:Make It Sans IS24 Web,Verdana,DejaVu Sans,Arial,Helvetica,sans-serif;font-size:1.6rem;padding:0 12px;transition:border .3s;width:100%}.RadioButton_select-container__-qm8A>.RadioButton_input-text__-vtHK,.RadioButton_select-container__-qm8A>.RadioButton_select__YQgVe,.RadioButton_select-container__-qm8A>.RadioButton_textarea__Nvz33{-webkit-appearance:none;appearance:none}@media (-ms-high-contrast:none){.RadioButton_select-container__-qm8A>.RadioButton_input-text__-vtHK,.RadioButton_select-container__-qm8A>.RadioButton_select__YQgVe,.RadioButton_select-container__-qm8A>.RadioButton_textarea__Nvz33{padding-right:0}.RadioButton_select-container__-qm8A>.RadioButton_input-text__-vtHK:after,.RadioButton_select-container__-qm8A>.RadioButton_select__YQgVe:after,.RadioButton_select-container__-qm8A>.RadioButton_textarea__Nvz33:after{display:none}}.RadioButton_input-text__-vtHK:focus,.RadioButton_input-text__-vtHK:hover,.RadioButton_select__YQgVe:focus,.RadioButton_select__YQgVe:hover,.RadioButton_textarea__Nvz33:focus,.RadioButton_textarea__Nvz33:hover{border-color:#333}.RadioButton_input-text__-vtHK:-ms-input-placeholder,.RadioButton_select__YQgVe:-ms-input-placeholder,.RadioButton_textarea__Nvz33:-ms-input-placeholder{color:#757575}.RadioButton_input-text__-vtHK::placeholder,.RadioButton_select__YQgVe::placeholder,.RadioButton_textarea__Nvz33::placeholder{color:#757575}.RadioButton_input-text__-vtHK:disabled,.RadioButton_select__YQgVe:disabled,.RadioButton_textarea__Nvz33:disabled{background-color:#f5f5f5;border-color:#ccc;color:#999}.RadioButton_input-text__-vtHK:disabled:-ms-input-placeholder,.RadioButton_select__YQgVe:disabled:-ms-input-placeholder,.RadioButton_textarea__Nvz33:disabled:-ms-input-placeholder{color:#999}.RadioButton_input-text__-vtHK:disabled::placeholder,.RadioButton_input-text__-vtHK:disabled~.RadioButton_input-label-helper-text__3nwre,.RadioButton_select__YQgVe:disabled::placeholder,.RadioButton_select__YQgVe:disabled~.RadioButton_input-label-helper-text__3nwre,.RadioButton_textarea__Nvz33:disabled::placeholder,.RadioButton_textarea__Nvz33:disabled~.RadioButton_input-label-helper-text__3nwre{color:#999}.RadioButton_input-text__-vtHK,.RadioButton_select__YQgVe{height:40px}.RadioButton_input-text__-vtHK:not(input):not(select),.RadioButton_select__YQgVe:not(input):not(select){line-height:40px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.RadioButton_textarea__Nvz33{padding-bottom:12px;padding-top:12px}.RadioButton_input-text__-vtHK.RadioButton_error__Y3SOS,.RadioButton_select__YQgVe.RadioButton_error__Y3SOS,.RadioButton_textarea__Nvz33.RadioButton_error__Y3SOS{border-color:#e74b3c}.RadioButton_input-text__-vtHK.RadioButton_success__6AULl,.RadioButton_textarea__Nvz33.RadioButton_success__6AULl{border-color:#00dc66}.RadioButton_radio-list__lP562 .RadioButton_radio-container__6wx-O{border-color:#e0e0e0}.RadioButton_radio-list__lP562 .RadioButton_radio-container__6wx-O:first-child{border-top-left-radius:2px;border-top-right-radius:2px}.RadioButton_radio-list__lP562 .RadioButton_radio-container__6wx-O:last-child{border-bottom:1px solid #e0e0e0;border-bottom-left-radius:2px;border-bottom-right-radius:2px}.RadioButton_radio-list__lP562 .RadioButton_radio-container__6wx-O:last-child .RadioButton_label-radio__tCsYt{padding-bottom:9px}.RadioButton_checkbox-list__ca07I .RadioButton_checkbox-container__49Ttv{border-color:#e0e0e0}.RadioButton_checkbox-list__ca07I .RadioButton_checkbox-container__49Ttv:first-child{border-top-left-radius:2px;border-top-right-radius:2px}.RadioButton_checkbox-list__ca07I .RadioButton_checkbox-container__49Ttv:last-child{border-bottom:1px solid #e0e0e0;border-bottom-left-radius:2px;border-bottom-right-radius:2px}.RadioButton_checkbox-list__ca07I .RadioButton_checkbox-container__49Ttv:last-child .RadioButton_label-checkbox__HTYEg{padding-bottom:9px}.RadioButton_toggle-switch-list__VuxOo .RadioButton_toggle-switch-container__3Afgi{border-color:#e0e0e0}.RadioButton_toggle-switch-list__VuxOo .RadioButton_toggle-switch-container__3Afgi:first-child{border-top-left-radius:2px;border-top-right-radius:2px}.RadioButton_toggle-switch-list__VuxOo .RadioButton_toggle-switch-container__3Afgi:last-child{border-bottom:1px solid #e0e0e0;border-bottom-left-radius:2px;border-bottom-right-radius:2px}.RadioButton_toggle-switch-list__VuxOo .RadioButton_toggle-switch-container__3Afgi:last-child .RadioButton_label-toggle-switch__X-OcB{padding-bottom:9px}.RadioButton_clickable-icon__I-jR3{cursor:pointer;pointer-events:visible!important}.RadioButton_input-label__6xuC2{padding-bottom:4px}.RadioButton_input-label__6xuC2.RadioButton_mandatory__L9M8g:after{color:#757575;content:"*";font-weight:400;margin-left:4px}.RadioButton_form__7iTWr label,.RadioButton_input-label__6xuC2,.RadioButton_label-checkbox__HTYEg,.RadioButton_label-radio__tCsYt,.RadioButton_label-toggle-switch__X-OcB{display:block;font-size:1.4rem;font-weight:600;line-height:20px}.RadioButton_label-optional__E3gTo:after{color:#757575;content:" (opt.)";font-weight:400}.RadioButton_input-label-helper-text__3nwre{color:#757575;display:inline-block;font-size:1.4rem;margin-top:6px}.RadioButton_gutter-form__niC2v .RadioButton_input-label-helper-text__3nwre{margin-bottom:-28px}.RadioButton_input-label-helper-text__3nwre:empty{display:inline!important}.RadioButton_radio-container__6wx-O{border:1px solid transparent;border-bottom:none;position:relative}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22{-webkit-appearance:none;appearance:none;height:2px;margin-top:10px;position:absolute;transition:box-shadow .3s}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked:disabled+.RadioButton_label-radio__tCsYt,.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt{color:#999}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt{font-weight:400;padding-bottom:10px;padding-top:9px}.RadioButton_radio-container__6wx-O{transition:background-color .3s}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22{width:2px}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt{margin-left:0;padding-left:35px;padding-right:11px}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before{border:1px solid #8f8f8f;content:"";margin-left:-24px;position:absolute;transition:background-color .3s}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before{background-color:#fff}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before{background-color:#242424}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt.RadioButton_error__Y3SOS:before,[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt.RadioButton_error__Y3SOS:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt.RadioButton_error__Y3SOS:before{border-color:#e74b3c}.RadioButton_radio-container__6wx-O:hover{background-color:initial}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22{border-radius:100%;margin-left:19px;top:8px}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:before{background-color:#00d9b1}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:before{border-color:#00d9b1}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:before{border-color:#757575}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:after{box-shadow:0 2px 4px 0 rgba(0,0,0,.15)}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:after,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:after{background-color:#fff}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:checked+.RadioButton_label-radio__tCsYt:after{background-color:#242424}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:active,.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:focus{box-shadow:0 0 0 14px rgba(0,217,177,.1)}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:focus:checked:not(:disabled)+.RadioButton_label-radio__tCsYt:before,.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:focus:not(:disabled)+.RadioButton_label-radio__tCsYt:before{border-color:#00d9b1}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:not(:disabled)+.RadioButton_label-radio__tCsYt:before,[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:not(:disabled)+.RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:not(:disabled)+.RadioButton_label-radio__tCsYt:before{border-color:#757575}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:not(:disabled)+.RadioButton_label-radio__tCsYt:after,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:not(:disabled)+.RadioButton_label-radio__tCsYt:after{background-color:#fff}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:not(:disabled)+.RadioButton_label-radio__tCsYt:after{background-color:#242424}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:checked:not(:disabled)+.RadioButton_label-radio__tCsYt:before{border-color:#00d9b1}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:checked:not(:disabled)+.RadioButton_label-radio__tCsYt:after,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:checked:not(:disabled)+.RadioButton_label-radio__tCsYt:after{background-color:#fff}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:hover:checked:not(:disabled)+.RadioButton_label-radio__tCsYt:after{background-color:#242424}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:before{border-color:#ccc}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:before{border-color:#757575}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:before{background-color:#e0e0e0}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:before{background-color:#c4c4c4}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:after,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:after{background-color:#e0e0e0}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled+.RadioButton_label-radio__tCsYt:after{background-color:#c4c4c4}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:before{border-color:#ccc}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:before{border-color:#676767}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:before{background-color:#ccc}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:before{background-color:#676767}.RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:after,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:after{background-color:#fff}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_input-radio__Q2N22:disabled:checked+.RadioButton_label-radio__tCsYt:after{background-color:#c4c4c4}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before{border-radius:100%;height:16px;margin-top:1px;width:16px}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before,[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:before{border-color:#757575}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:after{border-radius:100%;content:"";display:block;height:10px;margin-left:-20px;position:absolute;top:14px;transition:background-color .3s,border-color .3s;width:10px}.RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:after,[data-color-scheme=light] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:after{background-color:#fff}[data-color-scheme=dark] .RadioButton_radio-container__6wx-O .RadioButton_label-radio__tCsYt:after{background-color:#242424}</style><style type="text/css">.TextInput_input-text-container__N4X2Y,.TextInput_select-container__YdF9H,.TextInput_textarea-container__EdZPT{position:relative}.TextInput_input-text-container__N4X2Y>.TextInput_affix-left__gDqb7,.TextInput_input-text-container__N4X2Y>.TextInput_affix-right__sHMa3,.TextInput_input-text-container__N4X2Y>.TextInput_input-icon-left__ow-rZ,.TextInput_input-text-container__N4X2Y>.TextInput_input-icon-right__NdGL-,.TextInput_select-container__YdF9H>.TextInput_affix-left__gDqb7,.TextInput_select-container__YdF9H>.TextInput_affix-right__sHMa3,.TextInput_select-container__YdF9H>.TextInput_input-icon-left__ow-rZ,.TextInput_select-container__YdF9H>.TextInput_input-icon-right__NdGL-,.TextInput_textarea-container__EdZPT>.TextInput_affix-left__gDqb7,.TextInput_textarea-container__EdZPT>.TextInput_affix-right__sHMa3,.TextInput_textarea-container__EdZPT>.TextInput_input-icon-left__ow-rZ,.TextInput_textarea-container__EdZPT>.TextInput_input-icon-right__NdGL-{color:#333;font-size:24px;line-height:40px;margin-left:12px;margin-right:12px;pointer-events:none;position:absolute;z-index:1}.TextInput_input-text-container__N4X2Y>.TextInput_affix-left__gDqb7+.TextInput_select__rawpt,.TextInput_input-text-container__N4X2Y>.TextInput_affix-left__gDqb7~.TextInput_input-text__RsQrL,.TextInput_input-text-container__N4X2Y>.TextInput_affix-right__sHMa3+.TextInput_select__rawpt,.TextInput_input-text-container__N4X2Y>.TextInput_input-icon-left__ow-rZ+.TextInput_select__rawpt,.TextInput_input-text-container__N4X2Y>.TextInput_input-icon-left__ow-rZ~.TextInput_input-text__RsQrL,.TextInput_input-text-container__N4X2Y>.TextInput_input-icon-right__NdGL-+.TextInput_select__rawpt,.TextInput_select-container__YdF9H>.TextInput_affix-left__gDqb7+.TextInput_select__rawpt,.TextInput_select-container__YdF9H>.TextInput_affix-left__gDqb7~.TextInput_input-text__RsQrL,.TextInput_select-container__YdF9H>.TextInput_affix-right__sHMa3+.TextInput_select__rawpt,.TextInput_select-container__YdF9H>.TextInput_input-icon-left__ow-rZ+.TextInput_select__rawpt,.TextInput_select-container__YdF9H>.TextInput_input-icon-left__ow-rZ~.TextInput_input-text__RsQrL,.TextInput_select-container__YdF9H>.TextInput_input-icon-right__NdGL-+.TextInput_select__rawpt,.TextInput_textarea-container__EdZPT>.TextInput_affix-left__gDqb7+.TextInput_select__rawpt,.TextInput_textarea-container__EdZPT>.TextInput_affix-left__gDqb7~.TextInput_input-text__RsQrL,.TextInput_textarea-container__EdZPT>.TextInput_affix-right__sHMa3+.TextInput_select__rawpt,.TextInput_textarea-container__EdZPT>.TextInput_input-icon-left__ow-rZ+.TextInput_select__rawpt,.TextInput_textarea-container__EdZPT>.TextInput_input-icon-left__ow-rZ~.TextInput_input-text__RsQrL,.TextInput_textarea-container__EdZPT>.TextInput_input-icon-right__NdGL-+.TextInput_select__rawpt{padding-left:44px}.TextInput_input-text-container__N4X2Y>.TextInput_affix-right__sHMa3,.TextInput_input-text-container__N4X2Y>.TextInput_input-icon-right__NdGL-,.TextInput_select-container__YdF9H>.TextInput_affix-right__sHMa3,.TextInput_select-container__YdF9H>.TextInput_input-icon-right__NdGL-,.TextInput_textarea-container__EdZPT>.TextInput_affix-right__sHMa3,.TextInput_textarea-container__EdZPT>.TextInput_input-icon-right__NdGL-{right:0}.TextInput_input-text-container__N4X2Y>.TextInput_affix-right__sHMa3~.TextInput_input-text__RsQrL,.TextInput_input-text-container__N4X2Y>.TextInput_input-icon-right__NdGL-~.TextInput_input-text__RsQrL,.TextInput_select-container__YdF9H>.TextInput_affix-right__sHMa3~.TextInput_input-text__RsQrL,.TextInput_select-container__YdF9H>.TextInput_input-icon-right__NdGL-~.TextInput_input-text__RsQrL,.TextInput_textarea-container__EdZPT>.TextInput_affix-right__sHMa3~.TextInput_input-text__RsQrL,.TextInput_textarea-container__EdZPT>.TextInput_input-icon-right__NdGL-~.TextInput_input-text__RsQrL{padding-right:44px}.TextInput_input-text-container__N4X2Y>.TextInput_affix-unit__omvvD,.TextInput_select-container__YdF9H>.TextInput_affix-unit__omvvD,.TextInput_textarea-container__EdZPT>.TextInput_affix-unit__omvvD{font-size:16px;margin-left:auto;margin-right:auto;text-align:center;width:44px}.TextInput_input-text__RsQrL,.TextInput_select__rawpt,.TextInput_textarea__MBTYc{background-color:#fff;border:1px solid #adadad;border-radius:4px;caret-color:#333;color:#333;font-family:Make It Sans IS24 Web,Verdana,DejaVu Sans,Arial,Helvetica,sans-serif;font-size:1.6rem;padding:0 12px;transition:border .3s;width:100%}.TextInput_select-container__YdF9H>.TextInput_input-text__RsQrL,.TextInput_select-container__YdF9H>.TextInput_select__rawpt,.TextInput_select-container__YdF9H>.TextInput_textarea__MBTYc{-webkit-appearance:none;appearance:none}@media (-ms-high-contrast:none){.TextInput_select-container__YdF9H>.TextInput_input-text__RsQrL,.TextInput_select-container__YdF9H>.TextInput_select__rawpt,.TextInput_select-container__YdF9H>.TextInput_textarea__MBTYc{padding-right:0}.TextInput_select-container__YdF9H>.TextInput_input-text__RsQrL:after,.TextInput_select-container__YdF9H>.TextInput_select__rawpt:after,.TextInput_select-container__YdF9H>.TextInput_textarea__MBTYc:after{display:none}}.TextInput_input-text__RsQrL:focus,.TextInput_input-text__RsQrL:hover,.TextInput_select__rawpt:focus,.TextInput_select__rawpt:hover,.TextInput_textarea__MBTYc:focus,.TextInput_textarea__MBTYc:hover{border-color:#333}.TextInput_input-text__RsQrL:-ms-input-placeholder,.TextInput_select__rawpt:-ms-input-placeholder,.TextInput_textarea__MBTYc:-ms-input-placeholder{color:#757575}.TextInput_input-text__RsQrL::placeholder,.TextInput_select__rawpt::placeholder,.TextInput_textarea__MBTYc::placeholder{color:#757575}.TextInput_input-text__RsQrL:disabled,.TextInput_select__rawpt:disabled,.TextInput_textarea__MBTYc:disabled{background-color:#f5f5f5;border-color:#ccc;color:#999}.TextInput_input-text__RsQrL:disabled:-ms-input-placeholder,.TextInput_select__rawpt:disabled:-ms-input-placeholder,.TextInput_textarea__MBTYc:disabled:-ms-input-placeholder{color:#999}.TextInput_input-text__RsQrL:disabled::placeholder,.TextInput_input-text__RsQrL:disabled~.TextInput_input-label-helper-text__d3mae,.TextInput_select__rawpt:disabled::placeholder,.TextInput_select__rawpt:disabled~.TextInput_input-label-helper-text__d3mae,.TextInput_textarea__MBTYc:disabled::placeholder,.TextInput_textarea__MBTYc:disabled~.TextInput_input-label-helper-text__d3mae{color:#999}.TextInput_input-text__RsQrL,.TextInput_select__rawpt{height:40px}.TextInput_input-text__RsQrL:not(input):not(select),.TextInput_select__rawpt:not(input):not(select){line-height:40px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.TextInput_textarea__MBTYc{padding-bottom:12px;padding-top:12px}.TextInput_input-text__RsQrL.TextInput_error__EHKVv,.TextInput_select__rawpt.TextInput_error__EHKVv,.TextInput_textarea__MBTYc.TextInput_error__EHKVv{border-color:#e74b3c}.TextInput_input-text__RsQrL.TextInput_success__EOQZ7,.TextInput_textarea__MBTYc.TextInput_success__EOQZ7{border-color:#00dc66}.TextInput_radio-list__satho .TextInput_radio-container__NA4PO{border-color:#e0e0e0}.TextInput_radio-list__satho .TextInput_radio-container__NA4PO:first-child{border-top-left-radius:2px;border-top-right-radius:2px}.TextInput_radio-list__satho .TextInput_radio-container__NA4PO:last-child{border-bottom:1px solid #e0e0e0;border-bottom-left-radius:2px;border-bottom-right-radius:2px}.TextInput_radio-list__satho .TextInput_radio-container__NA4PO:last-child .TextInput_label-radio__P-e4D{padding-bottom:9px}.TextInput_checkbox-list__lpndX .TextInput_checkbox-container__xHVMc{border-color:#e0e0e0}.TextInput_checkbox-list__lpndX .TextInput_checkbox-container__xHVMc:first-child{border-top-left-radius:2px;border-top-right-radius:2px}.TextInput_checkbox-list__lpndX .TextInput_checkbox-container__xHVMc:last-child{border-bottom:1px solid #e0e0e0;border-bottom-left-radius:2px;border-bottom-right-radius:2px}.TextInput_checkbox-list__lpndX .TextInput_checkbox-container__xHVMc:last-child .TextInput_label-checkbox__-aJGk{padding-bottom:9px}.TextInput_toggle-switch-list__eIcpM .TextInput_toggle-switch-container__A6Fjh{border-color:#e0e0e0}.TextInput_toggle-switch-list__eIcpM .TextInput_toggle-switch-container__A6Fjh:first-child{border-top-left-radius:2px;border-top-right-radius:2px}.TextInput_toggle-switch-list__eIcpM .TextInput_toggle-switch-container__A6Fjh:last-child{border-bottom:1px solid #e0e0e0;border-bottom-left-radius:2px;border-bottom-right-radius:2px}.TextInput_toggle-switch-list__eIcpM .TextInput_toggle-switch-container__A6Fjh:last-child .TextInput_label-toggle-switch__fQTGK{padding-bottom:9px}.TextInput_clickable-icon__o4dJv{cursor:pointer;pointer-events:visible!important}.TextInput_input-label__e-ORN{padding-bottom:4px}.TextInput_input-label__e-ORN.TextInput_mandatory__b4IVP:after{color:#757575;content:"*";font-weight:400;margin-left:4px}.TextInput_form__UbAuJ label,.TextInput_input-label__e-ORN,.TextInput_label-checkbox__-aJGk,.TextInput_label-radio__P-e4D,.TextInput_label-toggle-switch__fQTGK{display:block;font-size:1.4rem;font-weight:600;line-height:20px}.TextInput_label-optional__JPS3k:after{color:#757575;content:" (opt.)";font-weight:400}.TextInput_input-label-helper-text__d3mae{color:#757575;display:inline-block;font-size:1.4rem;margin-top:6px}.TextInput_gutter-form__niDmh .TextInput_input-label-helper-text__d3mae{margin-bottom:-28px}.TextInput_input-label-helper-text__d3mae:empty{display:inline!important}input::-webkit-inner-spin-button,input::-webkit-outer-spin-button{-webkit-appearance:none}input[type=number]{-webkit-appearance:textfield;appearance:textfield}</style><style type="text/css">.Fonts_button-icon-standalone__nlwap.Fonts_disabled__8A5Iu,.Fonts_button-icon-standalone__nlwap.Fonts_disabled__8A5Iu:active,.Fonts_button-icon-standalone__nlwap.Fonts_disabled__8A5Iu:focus,.Fonts_button-icon-standalone__nlwap.Fonts_disabled__8A5Iu:hover,.Fonts_button-icon-standalone__nlwap.Fonts_disabled__8A5Iu:link,.Fonts_button-icon-standalone__nlwap.Fonts_disabled__8A5Iu:visited,.Fonts_link-text__jKRBr.Fonts_disabled__8A5Iu,.Fonts_link-text__jKRBr.Fonts_disabled__8A5Iu:active,.Fonts_link-text__jKRBr.Fonts_disabled__8A5Iu:focus,.Fonts_link-text__jKRBr.Fonts_disabled__8A5Iu:hover,.Fonts_link-text__jKRBr.Fonts_disabled__8A5Iu:link,.Fonts_link-text__jKRBr.Fonts_disabled__8A5Iu:visited,a.Fonts_disabled__8A5Iu,a.Fonts_disabled__8A5Iu:active,a.Fonts_disabled__8A5Iu:focus,a.Fonts_disabled__8A5Iu:hover,a.Fonts_disabled__8A5Iu:link,a.Fonts_disabled__8A5Iu:visited{color:#333;cursor:default;text-decoration:none}.Fonts_clearfix-before__G53PY:before,.Fonts_clearfix__Ledn7:after{clear:both;content:"";display:table}.Fonts_vertical-center-container__Z-QHo{height:100%}.Fonts_vertical-center-container__Z-QHo:after{content:"";height:100%}.Fonts_vertical-center-container__Z-QHo:after,.Fonts_vertical-center__6AfNm{display:inline-block;vertical-align:middle}.Fonts_horizontal-center__l2BU0{display:block;margin:0 auto}.Fonts_cursor-pointer__oXL-k{cursor:pointer}.Fonts_height-full__ZKeWE{height:100%}.Fonts_core-hide__GqXFW,[data-theme=core] .Fonts_core-hide__GqXFW{display:none}.Fonts_cosma-hide__bs3uo,[data-theme=core] .Fonts_cosma-hide__bs3uo,[data-theme=cosma] .Fonts_core-hide__GqXFW{display:initial}.Fonts_core-hide--inline__-4wnG,[data-theme=core] .Fonts_core-hide--inline__-4wnG,[data-theme=cosma] .Fonts_cosma-hide__bs3uo{display:none}.Fonts_cosma-hide--inline__8Mwgx,[data-theme=core] .Fonts_cosma-hide--inline__8Mwgx,[data-theme=cosma] .Fonts_core-hide--inline__-4wnG{display:inline}.Fonts_core-hide--block__EPqaa,[data-theme=core] .Fonts_core-hide--block__EPqaa,[data-theme=cosma] .Fonts_cosma-hide--inline__8Mwgx{display:none}.Fonts_cosma-hide--block__QO-C6,[data-theme=core] .Fonts_cosma-hide--block__QO-C6,[data-theme=cosma] .Fonts_core-hide--block__EPqaa{display:block}.Fonts_core-hide--inline-block__uHuR0,[data-theme=core] .Fonts_core-hide--inline-block__uHuR0,[data-theme=cosma] .Fonts_cosma-hide--block__QO-C6{display:none}.Fonts_cosma-hide--inline-block__x4ARn,[data-theme=core] .Fonts_cosma-hide--inline-block__x4ARn,[data-theme=cosma] .Fonts_core-hide--inline-block__uHuR0{display:inline-block}.Fonts_core-hide--flex__V-ufb,[data-theme=core] .Fonts_core-hide--flex__V-ufb,[data-theme=cosma] .Fonts_cosma-hide--inline-block__x4ARn{display:none}.Fonts_cosma-hide--flex__ArZSA,[data-theme=core] .Fonts_cosma-hide--flex__ArZSA,[data-theme=cosma] .Fonts_core-hide--flex__V-ufb{display:flex}.Fonts_core-hide--inline-flex__vRD2L,[data-theme=core] .Fonts_core-hide--inline-flex__vRD2L,[data-theme=cosma] .Fonts_cosma-hide--flex__ArZSA{display:none}.Fonts_cosma-hide--inline-flex__CP9F3,[data-theme=core] .Fonts_cosma-hide--inline-flex__CP9F3,[data-theme=cosma] .Fonts_core-hide--inline-flex__vRD2L{display:inline-flex}[data-theme=cosma] .Fonts_cosma-hide--inline-flex__CP9F3{display:none}.Fonts_font-h1__eX5Et{font-size:4rem;line-height:60px}.Fonts_font-h2__U-6iN{font-size:3.2rem;line-height:48px}.Fonts_font-h3__9ME0F{font-size:2.4rem;line-height:36px}.Fonts_font-h4__HAa3O{font-size:2rem;line-height:32px}.Fonts_font-h5__n9J2L,.Fonts_font-h6__Oh3iY{font-size:1.8rem;line-height:28px}.Fonts_font-h1__eX5Et,.Fonts_font-h2__U-6iN,.Fonts_font-h3__9ME0F{font-weight:700}.Fonts_font-h4__HAa3O,.Fonts_font-h5__n9J2L,.Fonts_font-h6__Oh3iY{font-weight:600}.Fonts_font-h1__eX5Et,.Fonts_font-h2__U-6iN,.Fonts_font-h3__9ME0F,.Fonts_font-h4__HAa3O,.Fonts_font-h5__n9J2L,.Fonts_font-h6__Oh3iY{margin-bottom:.4em}.Fonts_font-light__Td--z{font-weight:300!important}.Fonts_font-normal__i05Sj{font-weight:400!important}.Fonts_font-semibold__2GTa4{font-weight:600!important}.Fonts_font-bold__Qw6KZ{font-weight:800!important}.Fonts_font-italic__KuXKt{font-style:italic!important}.Fonts_font-strike__gm7pH{text-decoration:line-through!important}.Fonts_font-uppercase__GEC8G{text-transform:uppercase!important}.Fonts_font-capitalized__R-pop{text-transform:capitalize!important}.Fonts_font-brand-primary__-B-8O,.Fonts_font-brand__CTlSG,.Fonts_font-brandorange__F-nDl{color:#008289!important}.Fonts_font-error__j-bfx{color:#e74b3c!important}.Fonts_font-confirm__Jj4cP{color:#00d0b2!important}.Fonts_font-info__q-TnZ{color:#237fff!important}.Fonts_font-warning__iGgbs{color:#f2ca26!important}.Fonts_font-white__IB1-M{color:#fff!important}.Fonts_font-regular__-P0IK{color:#333!important}.Fonts_font-lightgray__o2UXY{color:#757575!important}.Fonts_font-nowrap__rxJ8C{white-space:nowrap!important}.Fonts_font-break-all__C3Lf0{word-break:break-all}.Fonts_font-ellipsis__ISp0m{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-break:normal}.Fonts_font-highlight__EYocZ{font-size:1.4rem;font-weight:600!important}.Fonts_font-tabular__c8PX6{font-size:1.4rem;line-height:1.4}.Fonts_font-hint__S23UH{font-size:1.2rem}.Fonts_font-center__bb0DH{text-align:center!important}.Fonts_font-left__7L4Nw{text-align:left!important}.Fonts_font-right__UQwBE{text-align:right!important}.Fonts_font-line-s__bhGgS,.Fonts_font-line-xs__asQ5F{line-height:1.4!important}.Fonts_font-line-standard__G-74H{line-height:1.61!important}</style><style type="text/css">.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:active,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:focus,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:hover,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:link,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:visited,.Button_link-text__MjJHt.Button_disabled__wwdZc,.Button_link-text__MjJHt.Button_disabled__wwdZc:active,.Button_link-text__MjJHt.Button_disabled__wwdZc:focus,.Button_link-text__MjJHt.Button_disabled__wwdZc:hover,.Button_link-text__MjJHt.Button_disabled__wwdZc:link,.Button_link-text__MjJHt.Button_disabled__wwdZc:visited,a.Button_disabled__wwdZc,a.Button_disabled__wwdZc:active,a.Button_disabled__wwdZc:focus,a.Button_disabled__wwdZc:hover,a.Button_disabled__wwdZc:link,a.Button_disabled__wwdZc:visited{color:#333;cursor:default;text-decoration:none}.Button_clearfix-before__Vcn7e:before,.Button_clearfix__rgtng:after{clear:both;content:"";display:table}.Button_vertical-center-container__-S0vv{height:100%}.Button_vertical-center-container__-S0vv:after{content:"";height:100%}.Button_vertical-center-container__-S0vv:after,.Button_vertical-center__5r377{display:inline-block;vertical-align:middle}.Button_horizontal-center__OEvUl{display:block;margin:0 auto}.Button_cursor-pointer__zzL8O{cursor:pointer}.Button_height-full__BUJgk{height:100%}.Button_core-hide__cE0Zd,[data-theme=core] .Button_core-hide__cE0Zd{display:none}.Button_cosma-hide__XyNRL,[data-theme=core] .Button_cosma-hide__XyNRL,[data-theme=cosma] .Button_core-hide__cE0Zd{display:initial}.Button_core-hide--inline__AAaa-,[data-theme=core] .Button_core-hide--inline__AAaa-,[data-theme=cosma] .Button_cosma-hide__XyNRL{display:none}.Button_cosma-hide--inline__icLpm,[data-theme=core] .Button_cosma-hide--inline__icLpm,[data-theme=cosma] .Button_core-hide--inline__AAaa-{display:inline}.Button_core-hide--block__a3Otm,[data-theme=core] .Button_core-hide--block__a3Otm,[data-theme=cosma] .Button_cosma-hide--inline__icLpm{display:none}.Button_cosma-hide--block__kiKm8,[data-theme=core] .Button_cosma-hide--block__kiKm8,[data-theme=cosma] .Button_core-hide--block__a3Otm{display:block}.Button_core-hide--inline-block__qHh5H,[data-theme=core] .Button_core-hide--inline-block__qHh5H,[data-theme=cosma] .Button_cosma-hide--block__kiKm8{display:none}.Button_cosma-hide--inline-block__-QcaH,[data-theme=core] .Button_cosma-hide--inline-block__-QcaH,[data-theme=cosma] .Button_core-hide--inline-block__qHh5H{display:inline-block}.Button_core-hide--flex__WlkUd,[data-theme=core] .Button_core-hide--flex__WlkUd,[data-theme=cosma] .Button_cosma-hide--inline-block__-QcaH{display:none}.Button_cosma-hide--flex__8SgQg,[data-theme=core] .Button_cosma-hide--flex__8SgQg,[data-theme=cosma] .Button_core-hide--flex__WlkUd{display:flex}.Button_core-hide--inline-flex__1PRjl,[data-theme=core] .Button_core-hide--inline-flex__1PRjl,[data-theme=cosma] .Button_cosma-hide--flex__8SgQg{display:none}.Button_cosma-hide--inline-flex__jSAg1,[data-theme=core] .Button_cosma-hide--inline-flex__jSAg1,[data-theme=cosma] .Button_core-hide--inline-flex__1PRjl{display:inline-flex}[data-theme=cosma] .Button_cosma-hide--inline-flex__jSAg1{display:none}.Button_button-inverted__NpoZk,.Button_button-primary__6QTnx,.Button_button-secondary__AVVwq,.Button_button-tertiary__kyqTu,.Button_button__DdOl8{-webkit-appearance:none;appearance:none;border:1px solid transparent;border-radius:8px;cursor:pointer;display:inline-block;font-family:Make It Sans IS24 Web,Verdana,DejaVu Sans,Arial,Helvetica,sans-serif;font-size:1.4rem;font-weight:600;letter-spacing:.2px;line-height:1.42857143em;min-width:7.14285714em;padding:.64285714em 1.64285714em;text-align:center;text-decoration:none;white-space:nowrap}.Button_button-inverted__NpoZk:focus,.Button_button-inverted__NpoZk:hover,.Button_button-primary__6QTnx:focus,.Button_button-primary__6QTnx:hover,.Button_button-secondary__AVVwq:focus,.Button_button-secondary__AVVwq:hover,.Button_button-tertiary__kyqTu:focus,.Button_button-tertiary__kyqTu:hover,.Button_button__DdOl8:focus,.Button_button__DdOl8:hover{text-decoration:none}.Button_button-inverted__NpoZk.Button_button-small__jQEcT,.Button_button-primary__6QTnx.Button_button-small__jQEcT,.Button_button-secondary__AVVwq.Button_button-small__jQEcT,.Button_button-tertiary__kyqTu.Button_button-small__jQEcT,.Button_button__DdOl8.Button_button-small__jQEcT{min-width:9.42857143em;padding-bottom:.35714286em;padding-top:.35714286em}.Button_button-inverted__NpoZk.Button_button-large__di5rZ,.Button_button-primary__6QTnx.Button_button-large__di5rZ,.Button_button-secondary__AVVwq.Button_button-large__di5rZ,.Button_button-tertiary__kyqTu.Button_button-large__di5rZ,.Button_button__DdOl8.Button_button-large__di5rZ{min-width:9.42857143em;padding-bottom:.92857143em;padding-top:.92857143em}.Button_button-inverted__NpoZk.Button_disabled__wwdZc,.Button_button-inverted__NpoZk[disabled],.Button_button-primary__6QTnx.Button_disabled__wwdZc,.Button_button-primary__6QTnx[disabled],.Button_button-secondary__AVVwq.Button_disabled__wwdZc,.Button_button-secondary__AVVwq[disabled],.Button_button-tertiary__kyqTu.Button_disabled__wwdZc,.Button_button-tertiary__kyqTu[disabled],.Button_button__DdOl8.Button_disabled__wwdZc,.Button_button__DdOl8[disabled]{background-color:#ccc;border-color:#ccc;color:#8f8f8f;cursor:default}.Button_button-inverted__NpoZk.Button_disabled__wwdZc:hover,.Button_button-inverted__NpoZk.Button_disabled__wwdZc:link,.Button_button-inverted__NpoZk.Button_disabled__wwdZc:visited,.Button_button-inverted__NpoZk[disabled]:hover,.Button_button-inverted__NpoZk[disabled]:link,.Button_button-inverted__NpoZk[disabled]:visited,.Button_button-primary__6QTnx.Button_disabled__wwdZc:hover,.Button_button-primary__6QTnx.Button_disabled__wwdZc:link,.Button_button-primary__6QTnx.Button_disabled__wwdZc:visited,.Button_button-primary__6QTnx[disabled]:hover,.Button_button-primary__6QTnx[disabled]:link,.Button_button-primary__6QTnx[disabled]:visited,.Button_button-secondary__AVVwq.Button_disabled__wwdZc:hover,.Button_button-secondary__AVVwq.Button_disabled__wwdZc:link,.Button_button-secondary__AVVwq.Button_disabled__wwdZc:visited,.Button_button-secondary__AVVwq[disabled]:hover,.Button_button-secondary__AVVwq[disabled]:link,.Button_button-secondary__AVVwq[disabled]:visited,.Button_button-tertiary__kyqTu.Button_disabled__wwdZc:hover,.Button_button-tertiary__kyqTu.Button_disabled__wwdZc:link,.Button_button-tertiary__kyqTu.Button_disabled__wwdZc:visited,.Button_button-tertiary__kyqTu[disabled]:hover,.Button_button-tertiary__kyqTu[disabled]:link,.Button_button-tertiary__kyqTu[disabled]:visited,.Button_button__DdOl8.Button_disabled__wwdZc:hover,.Button_button__DdOl8.Button_disabled__wwdZc:link,.Button_button__DdOl8.Button_disabled__wwdZc:visited,.Button_button__DdOl8[disabled]:hover,.Button_button__DdOl8[disabled]:link,.Button_button__DdOl8[disabled]:visited{background-color:#ccc;border-color:#ccc;box-shadow:none;color:#8f8f8f}a.Button_button-inverted__NpoZk,a.Button_button-primary__6QTnx,a.Button_button-secondary__AVVwq,a.Button_button-tertiary__kyqTu,a.Button_button__DdOl8{font-size:1.4rem;font-weight:600;text-decoration:none}.Button_button-inverted__NpoZk,.Button_button-inverted__NpoZk:link,.Button_button-inverted__NpoZk:visited,.Button_button__DdOl8,.Button_button__DdOl8:link,.Button_button__DdOl8:visited{background-color:transparent;border-color:#333;color:#333;text-decoration:none}.Button_button-inverted__NpoZk:hover,.Button_button__DdOl8:hover{background-color:#eaeaea;box-shadow:none;color:#333}.Button_button-primary__6QTnx,.Button_button-primary__6QTnx:link,.Button_button-primary__6QTnx:visited{background-color:#00ffd0;border-color:#00ffd0;color:#333}.Button_button-primary__6QTnx:hover{background-color:#00d9b1;border-color:#00d9b1;color:#333}.Button_button-secondary__AVVwq,.Button_button-secondary__AVVwq:link,.Button_button-secondary__AVVwq:visited{background-color:#333;border-color:#333;color:#fff}.Button_button-secondary__AVVwq:hover{background-color:#606060;border-color:#606060;color:#fff}.Button_button-tertiary__kyqTu,.Button_button-tertiary__kyqTu:link,.Button_button-tertiary__kyqTu:visited{background-color:#fff;border:none;color:#333}.Button_button-tertiary__kyqTu:hover{background-color:#eaeaea;border:none;color:#333}[data-color-scheme=dark] .Button_button-inverted__NpoZk,[data-color-scheme=dark] .Button_button-inverted__NpoZk:link,[data-color-scheme=dark] .Button_button-inverted__NpoZk:visited{background-color:transparent;border-color:#adadad;color:#fff}[data-color-scheme=dark] .Button_button-inverted__NpoZk:hover{background-color:transparent;border-color:#fff;color:#fff}.Button_button-icon-standalone__JnoFB{-webkit-appearance:none;appearance:none;background-color:transparent;background:transparent;border:none;color:#2267e8;cursor:pointer;font-family:Make It Sans IS24 Web,Verdana,DejaVu Sans,Arial,Helvetica,sans-serif;font-size:1em;font-weight:400;min-width:0;outline:none;text-decoration:none}.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:active,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:focus,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:hover,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:link,.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc:visited{color:#333;cursor:default;text-decoration:none}.Button_button-icon-standalone__JnoFB:active,.Button_button-icon-standalone__JnoFB:focus,.Button_button-icon-standalone__JnoFB:hover{color:#2267e8;text-decoration:underline}.Button_button-icon-standalone__JnoFB.Button_disabled__wwdZc,.Button_button-icon-standalone__JnoFB[disabled]{color:#999}.Button_button-icon-standalone__JnoFB.Button_link-underline__lbZco{text-decoration:underline}.Button_button-icon-standalone-small__w6ETz{font-size:1.4rem;letter-spacing:0;line-height:1;min-width:0;padding:8px;vertical-align:bottom}.Button_button-icon-standalone-medium__Eq8X4{letter-spacing:0;line-height:1;min-width:0;padding:9px;vertical-align:bottom}.Button_button-icon-standalone-medium__Eq8X4 [class*=" s24-icons-"],.Button_button-icon-standalone-medium__Eq8X4 [class*=is24-icon],.Button_button-icon-standalone-medium__Eq8X4 [class^=s24-icons-],.Button_button-icon-standalone-medium__Eq8X4 svg{font-size:2rem}.Button_button-icon-standalone-large__TyITQ{letter-spacing:0;line-height:1;min-width:0;padding:13px;vertical-align:bottom}.Button_button-icon-standalone-large__TyITQ [class*=" s24-icons-"],.Button_button-icon-standalone-large__TyITQ [class*=is24-icon],.Button_button-icon-standalone-large__TyITQ [class^=s24-icons-],.Button_button-icon-standalone-large__TyITQ svg{font-size:2rem}.Button_button-icon-standalone__JnoFB span{font-size:2.4rem}.Button_button-icon-standalone__JnoFB:hover{background:none;border:#333;box-shadow:none;text-decoration:none}.Button_button-margin-top__MJbSo{margin-top:16px!important}.Button_button-margin-bottom__62p0-{margin-bottom:16px!important}.Button_button-margin-vertical__2U3yu{margin-bottom:16px!important;margin-top:16px!important}.Button_button-margin-left__msEmJ{margin-left:16px!important}.Button_button-margin-right__DZwIv{margin-right:16px!important}.Button_button-margin-horizontal__yo-p9{margin-left:16px!important;margin-right:16px!important}.Button_button-margin__za5ue{margin:16px!important}.Button_button-icon-margin-right__4dC3c{margin-right:8px}.Button_button-icon-margin-left__q3jFU{margin-left:8px}.Button_link-text-secondary__ZbIzj,.Button_link-text__MjJHt{-webkit-appearance:none;appearance:none;background-color:transparent;border:none;color:#2267e8;cursor:pointer;font-family:Make It Sans IS24 Web,Verdana,DejaVu Sans,Arial,Helvetica,sans-serif;font-weight:400;outline:none;text-decoration:none}.Button_link-text__MjJHt:active,.Button_link-text__MjJHt:focus,.Button_link-text__MjJHt:hover{color:#2267e8;text-decoration:underline}.Button_link-text__MjJHt.Button_disabled__wwdZc,.Button_link-text__MjJHt[disabled]{color:#999}.Button_link-text__MjJHt.Button_link-underline__lbZco{text-decoration:underline}.Button_link-text-secondary__ZbIzj{color:#333}.Button_link-text-secondary__ZbIzj:active,.Button_link-text-secondary__ZbIzj:focus,.Button_link-text-secondary__ZbIzj:hover{color:#333;text-decoration:underline}</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.cockpit__clear-input-icon {
  display: none;
  cursor: pointer;
  position: absolute;
  right: 12px;
  top: auto;
  text-align: right;
  bottom: 0;
  font-size: 1.6rem;
  line-height: 40px;
}
.cockpit__clear-input-icon.input-icon-right {
  pointer-events: initial;
}
.cockpit__clear-input-icon:hover {
  display: inline-block;
}
/* Show icon only when the corresponding input has the user's focus */
.input-text:hover ~ .cockpit__clear-input-icon,
.input-text:focus ~ .cockpit__clear-input-icon,
.input-text:active ~ .cockpit__clear-input-icon {
  display: inline-block;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.ui-autocomplete {
  z-index: 11730002 !important;
}
.ui-widget {
  font-size: 1.4rem;
}
@media (max-width: 668px) {
  .ui-widget.ui-menu {
    max-width: 100%;
    overflow-x: auto;
  }
}
.ui-widget.ui-menu .ui-menu-item {
  padding: 0;
}
.ui-widget.ui-menu .ui-menu-item-wrapper {
  white-space: nowrap;
  border: none;
  margin: 0;
  padding: 8px 16px;
}
.ui-widget.ui-menu .ui-state-active {
  background-color: #eaeaea;
  margin: 0;
  padding: 8px 16px;
}
.ui-widget.ui-menu .ui-autocomplete-category {
  color: #969696;
  padding: 8px;
}
.ui-front {
  z-index: auto;
}
.input-text.gac-field {
  text-overflow: ellipsis;
  padding-right: 32px;
}
</style><style>.ChipsAsRadio__chipRadio > input[type='radio'] {
  display: none;
}
.ChipsAsRadio__chipRadio > input[type='radio'] + label {
  border: 1px solid #C4C4C4;
  border-radius: 30px;
  background-color: #FFFFFF;
  cursor: pointer;
}
.ChipsAsRadio__chipRadio > input[type='radio']:checked + label {
  font-weight: 600;
  border: 1px solid #00d9b1;
  background-color: #e7fdf1;
}
</style><style>.PriceInsights__homeOwnerWorldStickyButtonContainer {
  padding: 0 16px;
  position: fixed;
  bottom: 0;
  background: #FFFFFF;
  box-shadow: 1px -20px 20px -2px rgba(0, 0, 0, 0.08);
  z-index: 1;
}
@media (max-width: 359px) {
  .PriceInsights__homeOwnerWorldStickyButtonContainer .PriceInsights__homeOwnerWorldStickyTooltipContainer {
    display: none;
  }
}
.PriceInsights__homeOwnerWorldStickyButtonContainer .PriceInsights__homeOwnerWorldStickyTooltipContainer .PriceInsights__homeOwnerWorldStickyTooltip {
  box-shadow: 0 1px 4px -1px rgba(0, 0, 0, 0.8);
  width: 222px;
  font-size: 12px;
  bottom: 120% !important;
}
.PriceInsights__homeOwnerWorldStickyButtonContainer .PriceInsights__homeOwnerWorldStickyTooltipContainer .PriceInsights__homeOwnerWorldStickyTooltip::after {
  border-color: #FFFFFF !important;
  box-shadow: -1px 1px 1px -0.5px rgba(0, 0, 0, 0.5);
}
.PriceInsights__homeOwnerWorldStickyButtonContainer .PriceInsights__homeOwnerWorldStickyTooltipContainer .PriceInsights__homeOwnerWorldStickyTooltip[data-show-tooltip="true"] {
  visibility: visible !important;
  opacity: 1 !important;
}
</style><style type="text/css">.Tooltip_tooltip-container__95u5X{height:100%;position:relative;width:100%}.Tooltip_tooltip-target__t19TW{height:100%;line-height:1;width:100%}.Tooltip_tooltip-container__95u5X .Tooltip_tooltip__T2FSA{background:#242424;border-radius:4px;opacity:0;padding:10px 16px;position:absolute;visibility:hidden;z-index:2}.Tooltip_tooltip-container__95u5X .Tooltip_tooltip__T2FSA:after{border:5px solid;content:"";position:absolute;transform:rotate(-45deg);transform-origin:0 0}.Tooltip_tooltip-container__95u5X:hover .Tooltip_tooltip__T2FSA{opacity:1;visibility:visible}.Tooltip_tooltip__T2FSA.Tooltip_positioning-top__0CGs2{bottom:90%;left:50%;transform:translateX(-50%)}.Tooltip_tooltip__T2FSA.Tooltip_positioning-top__0CGs2:after{border-color:transparent transparent #242424 #242424;bottom:-9px}.Tooltip_tooltip__T2FSA.Tooltip_positioning-bottom__rXe53{left:50%;top:90%;transform:translateX(-50%)}.Tooltip_tooltip__T2FSA.Tooltip_positioning-bottom__rXe53:after{border-color:#242424 #242424 transparent transparent;top:1px}.Tooltip_tooltip__T2FSA.Tooltip_positioning-left__3iq2K{right:98%;top:50%;transform:translateY(-50%)}.Tooltip_tooltip__T2FSA.Tooltip_positioning-left__3iq2K:after{border-color:transparent #242424 #242424 transparent;bottom:calc(50% - 10px);right:-2px}.Tooltip_tooltip__T2FSA.Tooltip_positioning-right__2UnWC{left:98%;top:50%;transform:translateY(-50%)}.Tooltip_tooltip__T2FSA.Tooltip_positioning-right__2UnWC:after{border-color:#242424 transparent transparent #242424;bottom:calc(50% - 10px);left:-6px}.Tooltip_tooltip__T2FSA.Tooltip_positioning-bottom__rXe53.Tooltip_arrow-left__0rqBW,.Tooltip_tooltip__T2FSA.Tooltip_positioning-top__0CGs2.Tooltip_arrow-left__0rqBW{left:calc(50% - 26px);transform:translateX(0)}.Tooltip_tooltip__T2FSA.Tooltip_positioning-bottom__rXe53.Tooltip_arrow-left__0rqBW:after,.Tooltip_tooltip__T2FSA.Tooltip_positioning-top__0CGs2.Tooltip_arrow-left__0rqBW:after{left:17px}.Tooltip_tooltip__T2FSA.Tooltip_positioning-bottom__rXe53.Tooltip_arrow-center__imaZG:after,.Tooltip_tooltip__T2FSA.Tooltip_positioning-top__0CGs2.Tooltip_arrow-center__imaZG:after{left:calc(50% - 7px)}.Tooltip_tooltip__T2FSA.Tooltip_positioning-bottom__rXe53.Tooltip_arrow-right__517tl,.Tooltip_tooltip__T2FSA.Tooltip_positioning-top__0CGs2.Tooltip_arrow-right__517tl{left:calc(50% + 23px);transform:translateX(-100%)}.Tooltip_tooltip__T2FSA.Tooltip_positioning-bottom__rXe53.Tooltip_arrow-right__517tl:after,.Tooltip_tooltip__T2FSA.Tooltip_positioning-top__0CGs2.Tooltip_arrow-right__517tl:after{right:20px}</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.status-message-layer {
  overflow: auto;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 11730000;
  background-color: rgba(44, 44, 44, 0.75);
  -webkit-overflow-scrolling: touch;
}
@media (max-width: 668px) {
  .status-message-layer .status-message-inner {
    padding-left: 16px;
    padding-right: 16px;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.cockpit__cockpit-close-icon {
  position: absolute;
  z-index: 1;
  top: 0;
  right: 0;
  padding: 16px;
  width: 54px;
  height: 54px;
  cursor: pointer;
  color: #333333;
}
.cockpit__cockpit-close-icon:hover,
.cockpit__cockpit-close-icon:focus,
.cockpit__cockpit-close-icon:active {
  text-decoration: none;
  color: #333333;
}
.cockpit__cockpit-close-icon--light,
.cockpit__cockpit-close-icon--dark {
  border-radius: 50%;
}
.cockpit__cockpit-close-icon--light {
  background-color: rgba(255, 255, 255, 0.8);
  color: #333333;
}
.cockpit__cockpit-close-icon--light:hover,
.cockpit__cockpit-close-icon--light:focus,
.cockpit__cockpit-close-icon--light:active {
  color: #333333;
}
.cockpit__cockpit-close-icon--dark {
  background-color: rgba(76, 76, 76, 0.8);
  color: #fff;
}
.cockpit__cockpit-close-icon--dark:hover,
.cockpit__cockpit-close-icon--dark:focus,
.cockpit__cockpit-close-icon--dark:active {
  color: #fff;
}
.cockpit__cockpit-close-icon:before,
.cockpit__cockpit-close-icon:after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -1px;
  margin-left: -11px;
  width: 22px;
  height: 2px;
  background-color: currentColor;
}
.cockpit__cockpit-close-icon:before {
  -webkit-transform: rotate(-45deg);
  -moz-transform: rotate(-45deg);
  -ms-transform: rotate(-45deg);
  -o-transform: rotate(-45deg);
  transform: rotate(-45deg);
}
.cockpit__cockpit-close-icon:after {
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
  transform: rotate(45deg);
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.slide-in-layer {
  visibility: hidden;
}
.slide-in-layer--open {
  visibility: visible;
}
.slide-in-layer .slide-in-layer-main {
  height: 100%;
  width: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  padding-top: 54px;
}
.slide-in-layer {
  position: fixed;
  z-index: 11730001;
  top: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  width: 100vw;
}
.slide-in-layer {
  left: 100%;
  transition: left 150ms ease-in;
}
.slide-in-layer--open {
  left: 0;
}
@supports (transform: translateX(0)) {
  .slide-in-layer {
    left: 0;
    transition: none;
  }
  .slide-in-layer {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
    transition: visibility 150ms ease-in, transform 150ms ease-in;
  }
  .slide-in-layer--open {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
.slide-in-layer {
  background-color: white;
}
.cockpit-layer-footer--hide-when-slide-in-layer-open {
  visiblity: visible;
  transition: visibility 150ms ease-in;
}
.slide-in-layer-open .cockpit-layer-footer--hide-when-slide-in-layer-open {
  visibility: hidden;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.cockpit-layer-footer-container {
  padding-bottom: 65px;
}
.cockpit-layer-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
}
.cockpit-layer-footer > .grid {
  height: 100%;
}
.cockpit-layer-footer--sticky {
  position: fixed;
  bottom: 0;
  max-width: 760px;
  z-index: 11730001;
}
.cockpit-layer-footer-controls {
  height: 65px;
  padding: 12px;
}
@media (min-width: 669px) {
  .cockpit-layer-footer-controls {
    height: 65px;
    padding: 12px 36px;
    border-radius: 0px 0px 12px 12px;
  }
}
.cockpit-layer-footer-controls--background-light {
  background-color: rgba(255, 255, 255, 0.8);
}
.cockpit-layer-footer-controls--background-dark {
  background-color: rgba(244, 246, 248, 0.8);
}
.cockpit-layer-footer-controls--background-dark .cockpit-layer-footer__opaque-background {
  background-color: #f6f8f9;
}
.cockpit-layer-footer-controls--background-light .cockpit-layer-footer__opaque-background {
  background-color: #ffffff;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.drop-down-layer-container {
  position: relative;
}
.drop-down-layer-container .drop-down-layer {
  transition: 300ms border;
  border: 1px solid #d6d6d6;
}
.drop-down-layer-container .input-icon-left {
  top: 0;
  z-index: 103;
}
.drop-down-layer {
  position: absolute;
  z-index: 101;
  min-width: 320px;
  width: 120%;
  background-color: #fff;
  top: calc(40px + 8px - 1px);
  box-shadow: 2px 2px 2px 0 rgba(0, 0, 0, 0.1);
  border-radius: 4px;
}
@media (min-width: 669px) and (max-width: 1013px) {
  .drop-down-layer.normal-width {
    min-width: 270px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .drop-down-layer.region-selection-width {
    min-width: 340px;
  }
}
@media (min-width: 1014px) {
  .drop-down-layer.region-selection-width {
    min-width: 380px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .drop-down-layer.region-selection--four-tabs {
    min-width: 380px;
  }
}
@media (min-width: 1014px) {
  .drop-down-layer.region-selection--four-tabs {
    min-width: 420px;
  }
}
.drop-down-layer__title {
  box-shadow: 1px 0 0 0 rgba(0, 0, 0, 0.1);
  z-index: 102;
  cursor: pointer;
  margin-bottom: -0.5em;
  position: relative;
}
.drop-down-layer__title:after {
  position: absolute;
  top: 50%;
  right: 12px;
  margin-top: -0.5em;
  line-height: 1;
  content: "\eae2";
  font-family: s24-icons;
  font-size: 1.6rem;
  cursor: pointer;
  pointer-events: none;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.cockpit__region-selection-tab svg {
  display: block;
  margin: 0 auto;
}
@media (max-width: 668px) {
  .cockpit__region-selection-tab span {
    font-size: 10px;
  }
}
@media (min-width: 669px) {
  .cockpit__region-selection-tab span {
    font-size: 11px;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.region-tag-list > li {
  display: inline-block;
  padding: 0.25em 0.5em;
  margin-top: 8px;
  margin-right: 0.6em;
  background-color: #eaeaea;
  border-radius: 4px;
}
.region-tag-list > li:last-child {
  margin-right: 0;
}
.region-tag-list > li.region-tag-item {
  color: #fff;
  background-color: #333333;
  border-radius: 4px;
  cursor: pointer;
}
.region-tag-list > li.region-tag-item.disabled {
  cursor: auto;
}
.cockpit__geo-hierarchy-selection-list {
  overflow-x: hidden;
}
@media (min-width: 669px) {
  .cockpit__geo-hierarchy-selection-list {
    max-height: 246px;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }
}
@media (max-width: 668px) {
  .cockpit__geo-hierarchy-selection-list {
    width: 100%;
  }
}
.cockpit__geo-hierarchy-selection-list label {
  cursor: pointer;
}
.cockpit__geo-hierarchy-selection-list label .count {
  color: #2267e8;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.select-buttons__container {
  position: relative;
  overflow: hidden;
  border: 1px solid #cacaca;
  border-left: none;
  float: left;
}
.select-buttons__container:first-child {
  border-left: 1px solid #cacaca;
}
.select-buttons__container:before {
  content: "";
  display: block;
  padding-top: 32px;
}
.select-buttons {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}
.select-buttons .select-buttons__inner-container {
  display: table;
  width: 100%;
  height: 32px;
}
.select-buttons span {
  cursor: pointer;
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
.select-buttons.selected {
  background-color: #747474;
}
.select-buttons.selected span {
  color: #fff;
}
.select-buttons--disabled .select-buttons__container {
  border-color: #d4d4d4;
  color: #d4d4d4;
  cursor: default;
}
.select-buttons--disabled .select-buttons span {
  cursor: auto;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.googlemap-field-container {
  margin-top: 4px;
  border: 1px solid #cacaca;
  background-color: #f4f6f8;
}
@media (max-width: 668px) {
  .googlemap-field-container {
    min-height: 10em;
  }
}
@media (min-width: 669px) {
  .googlemap-field-container {
    min-height: 14em;
  }
}
.googlemap-field {
  display: block;
  margin: 0 auto;
  max-width: 100%;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
@media (max-width: 668px) {
  .cockpit__region-selection-tabs {
    padding-bottom: 73px;
  }
}
.cockpit__region-selection-tab-list {
  border-bottom: 1px solid #A3A3A3;
}
.cockpit__region-selection-tab-list > .grid-item {
  margin-right: 6px;
}
@media (max-width: 668px) {
  .cockpit__region-selection-tab-list > .grid-item {
    margin-right: 4px;
  }
}
.cockpit__region-selection-tab-list > .grid-item:last-child {
  margin-right: 0;
}
.cockpit__region-selection-tab-container {
  border-top: 1px solid #A3A3A3;
  position: relative;
}
.cockpit__region-selection-tab-container[aria-selected=true] {
  border-top: 4px solid #00ffd0;
}
.cockpit__region-selection-tab {
  border: 0 solid #A3A3A3;
  border-width: 0 1px;
  padding-top: 8px;
  padding-bottom: 8px;
  min-width: 65px;
  text-align: center;
  cursor: pointer;
  background-color: #f2f2f2;
  border-bottom: 1px solid #A3A3A3;
  margin-bottom: -1px;
}
[aria-selected=true] .cockpit__region-selection-tab {
  background-color: #fff;
  color: #333333;
  padding-bottom: 6px;
  border-bottom-color: #fff;
}
[aria-selected=true] .cockpit__region-selection-tab svg {
  margin-top: -1px;
}
[role=tab]:hover .cockpit__region-selection-tab,
[role=tab]:focus .cockpit__region-selection-tab {
  color: #333333;
}
[aria-disabled=true] .cockpit__region-selection-tab,
[aria-disabled=true]:hover .cockpit__region-selection-tab,
[aria-disabled=true]:focus .cockpit__region-selection-tab {
  color: #d4d4d4;
  background-color: #fff;
  cursor: default;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.drawASearchMap {
  -webkit-overflow-scrolling: touch;
}
.drawASearchMap .drawASearchMapCloseButton {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 1;
  background-color: #747474;
  border-style: none;
  border-radius: 20px;
  padding: 8px 9px;
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.7);
  line-height: 1em;
}
.drawASearchMap .drawASearchMapCloseButton svg polygon {
  fill: white;
}
.drawASearchMap .drawASearchMapControls {
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translate(-50%, 0);
  padding-bottom: 16px;
}
.drawASearchPanel .drawASearchPanel_mapContainer {
  border: 1px solid #cacaca;
  background-color: #f4f6f8;
}
.drawASearchPanel .drawASearchPanel_mapContainer .drawASearchPanel_mapContainer_ratioBox {
  max-height: 229px;
  overflow: hidden;
}
.drawASearchPanel .drawASearchPanel_mapContainer .drawASearchPanel_mapContainer_ratioBox .drawASearchPanel_mapContainer_ratioBoxInner {
  padding-top: 59.6354167%;
}
.drawASearchPanel .drawASearchPanel_mapContainer img {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, 0);
  max-width: 100%;
  display: block;
  margin: 0 auto;
}
.confirmOverlayHeadline {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 8px;
  margin-right: 16px;
}
.confirmOverlayText {
  margin-bottom: 16px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.price-histogram__wrapper {
  margin-left: 4px !important;
  margin-right: 4px !important;
}
</style><style type="text/css">.Slider_screenreader-only__Zv1G4{clip:rect(0,0,0,0);border:0;height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.Slider_slider__UspdF{align-items:center;display:flex;height:50px;position:relative;z-index:1}.Slider_slider__UspdF.Slider_dragged__rvsOy .Slider_tooltip__zRFZ4{opacity:1!important}.Slider_slider__UspdF .Slider_range-bg__aP84N{background:#ccc;width:100%}.Slider_slider__UspdF .Slider_range-bg__aP84N,.Slider_slider__UspdF .Slider_range-max-limiter__JRC2i,.Slider_slider__UspdF .Slider_range-min-limiter__fDWVw{height:4px}.Slider_slider__UspdF .Slider_range-max-limiter__JRC2i,.Slider_slider__UspdF .Slider_range-min-limiter__fDWVw{background:#ccc;left:0;position:absolute;width:40%;z-index:3}.Slider_slider__UspdF .Slider_range-max-limiter__JRC2i{background:#00d9b1;width:70%;z-index:2}.Slider_slider__UspdF .Slider_range-limiter-handler__iuLmc{align-items:center;display:flex;height:100%;justify-content:center;margin-left:-12px;position:absolute;top:0;width:auto}@media (max-width:1013px){.Slider_slider__UspdF .Slider_range-limiter-handler__iuLmc{margin-left:-25px;width:50px}}.Slider_slider__UspdF .Slider_range-limiter-button__coDX-{background:#fff;border:0;border-radius:100px;box-shadow:0 0 0 1px rgba(0,0,0,.17);cursor:move;cursor:grab;height:24px;outline:none;padding:0;width:24px;z-index:4}.Slider_slider__UspdF .Slider_range-limiter-button__coDX-:hover{box-shadow:0 0 0 5px rgba(0,0,0,.17)}.Slider_slider__UspdF .Slider_range-limiter-button__coDX-:active{cursor:move;cursor:grabbing}.Slider_slider-label__bd-cr{clip:rect(0,0,0,0);border:0;height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
div[class^="Slider_slider" i] {
  margin-left: 12px !important;
  margin-right: 12px !important;
}
div[class^="Slider_range-min-limiter" i] {
  left: -12px !important;
  position: absolute !important;
}
div[class^="Slider_range-bg" i] {
  left: 12px !important;
  position: absolute !important;
}
</style><style>/* stylelint-disable-line */
.autosuggest-suggest-container {
  border: 1px solid #d5d5d5;
  border-top: none;
  position: absolute;
  background-color: #fff;
  top: 0;
  padding-top: 7px;
  padding-bottom: 8px;
  z-index: 1;
}
.autosuggest-suggest-line {
  padding-left: 12px;
  padding-top: 2px;
  padding-bottom: 2px;
  padding-right: 0px;
  background-color: #fff;
  width: 100%;
  outline: none;
  font-family: 'Open Sans', Verdana, 'DejaVu Sans', Arial, Helvetica, sans-serif;
  text-align: left;
  border: none;
  color: #000;
  white-space: nowrap;
  font-weight: normal;
  vertical-align: baseline;
}
.autosuggest-suggest-line:hover {
  background-color: #e0e0e0;
}
.autosuggest-suggest-line.autosuggest-suggest-line-selected {
  background-color: #e0e0e0;
}
.autosuggest-suggest-line.autosuggest-suggest-line-used {
  color: rgba(160, 40, 180, 0.86);
}
.autosuggest-suggest-tags-container {
  margin-top: 2px;
}
.autosuggest-suggest-tag {
  background-color: #dfdfdf;
  color: #343434;
  padding-left: 8px;
  padding-right: 27px;
  padding-top: 4px;
  padding-bottom: 4px;
  margin-right: 8px;
  margin-bottom: 2px;
  border-radius: 4px;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  position: relative;
}
.autosuggest-suggest-tag .autosuggest-suggest-tag-remove-btn {
  padding: 0;
  margin: 0;
  height: 16px !important;
  width: 16px;
  position: absolute;
  outline: none;
  right: 5px;
  top: 6px;
}
.autosuggest-suggest-tag .autosuggest-suggest-tag-remove-btn img {
  height: 16px;
  width: 16px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.energyEfficiencySelectionBox {
  border: 1px solid #e0e0e0;
  background: #fff;
  width: 100%;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox {
  width: 100%;
}
@media (max-width: 668px) {
  .energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox ul {
    max-height: 112px;
  }
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer {
  border-bottom: 1px solid #e0e0e0;
  max-height: 100px;
  overflow-y: scroll;
  overflow-x: hidden;
  -webkit-column-width: auto !important;
  -moz-column-width: auto !important;
  column-width: auto !important;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_A_PLUS {
  background-color: #247e34;
  border-left-color: #247e34;
  width: 2em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_A {
  background-color: #4f9d2a;
  border-left-color: #4f9d2a;
  width: 2.5em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_B {
  background-color: #91b41e;
  border-left-color: #91b41e;
  width: 3em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_C {
  background-color: #e1d506;
  border-left-color: #e1d506;
  width: 3.5em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_D {
  background-color: #f6e80f;
  border-left-color: #f6e80f;
  width: 4em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_E {
  background-color: #f5a60a;
  border-left-color: #f5a60a;
  width: 4.5em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_F {
  background-color: #e54e1f;
  border-left-color: #e54e1f;
  width: 5em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_G {
  background-color: #df201f;
  border-left-color: #df201f;
  width: 5.5em;
}
.energyEfficiencySelectionBox .energyEfficiencySelectionInnerBox .energyEfficiencyClassesContainer .E_CLASS_H {
  background-color: #df201f;
  border-left-color: #df201f;
  width: 6em;
}
.energyEfficiencySelectionBox .energyEfficiencyCloseBox {
  height: 30px;
  position: relative;
}
.energyEfficiencySelectionBox .energyEfficiencyCloseBox .close {
  height: 20px;
  right: 16px;
}
.energyClassLabel {
  padding-left: 3px;
  color: #fff;
  height: 20px;
  line-height: 20px;
}
.energyClassLabel::after {
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  border-left: 10px solid;
  border-left-color: inherit;
  content: '';
  float: right;
  margin-right: -10px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.react-cockpit [data-toggle="tooltip"] {
  cursor: pointer;
}
.react-cockpit optgroup {
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
}
.react-cockpit input:invalid {
  box-shadow: none;
  background-color: #ffdddc;
  border-color: #c42525;
}
.react-cockpit .fake-dropdown select {
  border-radius: 4px;
  width: 100%;
}
.react-cockpit .select {
  padding-right: 30px;
}
.react-cockpit .fake-dropdown::after {
  position: absolute;
  top: 50%;
  right: 12px;
  margin-top: -0.5em;
  line-height: 1;
  content: "\eadc";
  font-family: s24-icons;
  font-size: 1.6rem;
  cursor: pointer;
  pointer-events: none;
}
.react-cockpit input[type="text"],
.react-cockpit input[type="number"] {
  border-radius: 4px;
}
.react-cockpit .criterion {
  padding-bottom: 24px;
  position: relative;
}
.react-cockpit .font-disabled {
  color: #d4d4d4;
}
@media (min-width: 669px) {
  .react-cockpit .criterion {
    padding-bottom: 32px;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.cxp-map-draw-button {
  outline: none;
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  margin: 0 16px 2px 0;
}
.cxp-map-draw-centerbox {
  position: absolute;
  left: 50% !important;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
}
.cxp-map-draw-centerbox .cxp-map-draw-info-outer {
  margin-top: 16px;
  min-width: 122px;
  height: 33px;
}
@media (max-width: 668px) {
  .cxp-map-draw-centerbox .cxp-map-draw-info-outer {
    height: 52px;
  }
}
.cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-left {
  top: 0;
  height: 100%;
  left: -17px;
  width: 33px;
  z-index: -1;
  border-top-left-radius: 50%;
  border-bottom-left-radius: 50%;
}
@media (max-width: 668px) {
  .cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-left {
    left: -26px;
    width: 52px;
  }
}
.cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-right {
  top: 0;
  height: 100%;
  right: -17px;
  width: 33px;
  z-index: -1;
  border-top-right-radius: 50%;
  border-bottom-right-radius: 50%;
}
@media (max-width: 668px) {
  .cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-right {
    right: -26px;
    width: 52px;
  }
}
.cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-text {
  height: 33px;
  font-size: 1.4rem;
  font-family: "Make It Sans IS24 Web", "Verdana", "DejaVu Sans", "Arial", "Helvetica", sans-serif;
  text-align: center;
}
@media (max-width: 668px) {
  .cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-text {
    height: 52px;
  }
}
@media (min-width: 669px) {
  .cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-text {
    white-space: nowrap;
  }
}
.cxp-map-draw-centerbox .cxp-map-draw-info-outer .cxp-map-draw-info-text .loader.loader-small {
  width: 16px;
  height: 16px;
  background-size: 16px;
}
</style><style>/* stylelint-disable-line */
.overlayBackground {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(44, 44, 44, 0.75);
  z-index: 11730002;
  overflow: auto;
}
.overlayContentBox {
  min-width: 288px;
  padding: 24px;
  background: #fff;
  position: absolute;
  top: 50% !important;
  left: 50% !important;
  -webkit-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -ms-transform: translateX(-50%) translateY(-50%);
  -o-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}
@media (max-width: 668px) {
  .responsiveOverlayContentBox {
    margin: 0;
    min-height: 100%;
    min-width: 100%;
  }
}
.responsiveOverlayButtonReset {
  text-align: left;
  background: none;
  border: none;
  padding: 0;
  color: #2a7cca;
  font-weight: normal;
  vertical-align: baseline;
}
@media (min-width: 1014px) {
  .responsiveOverlayButtonReset {
    color: #ff7500;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.cockpit__realestate-type-layout {
  padding: 16px;
}
@media (min-width: 669px) {
  .cockpit__realestate-type-layout {
    padding: 32px;
    border-radius: 12px;
  }
  .cockpit__realestate-type-layout.tabbed-layout {
    padding: 24px;
  }
}
.cockpit__realestate-type-layout__separator {
  height: 8px;
  width: 100%;
  position: absolute;
  left: 0;
  background: #f5f5f5;
  box-shadow: 0px -1px 0px 0px #e0e0e0;
}
.cockpit__realestate-type-layout__title {
  display: inline-block;
}
.fix-collapsing-margins {
  padding: 1px;
  margin: -1px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
@media (min-width: 1014px) {
  .react-cockpit .cockpit-layer {
    padding-top: 30px;
  }
}
@media (max-width: 1013px) {
  .react-cockpit .cockpit-layer {
    padding-top: 0;
  }
}
.react-cockpit .cockpit-layer-container {
  overflow: auto;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 11730000;
  background-color: rgba(44, 44, 44, 0.75);
  -webkit-overflow-scrolling: touch;
}
@media (max-width: 668px) {
  body.slide-in-layer-open .react-cockpit .cockpit-layer-container {
    overflow: hidden;
  }
}
.react-cockpit .cockpit-layer-container-inner {
  height: 100%;
}
.react-cockpit .cockpit-layer {
  position: relative;
  z-index: 11730001;
  margin-left: auto;
  margin-right: auto;
  max-width: 760px;
  height: 100%;
}
.react-cockpit .cockpit-layer-footer-container {
  min-height: 100%;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.5);
  background: #fff;
  border-radius: 12px;
}
@media (min-width: 669px) {
  .react-cockpit .cockpit-layer-footer-container {
    height: 100%;
    min-height: 750px;
  }
}
body.no-scroll {
  position: fixed;
  overflow: hidden;
  width: 100%;
  height: 100%;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.textarea {
  height: 116px;
}
@media (max-width: 668px) {
  .textarea {
    height: 129px;
  }
}
.container-loading-icon {
  display: flex;
  justify-content: center;
  align-items: center;
}
.container-flex {
  display: flex;
  align-items: flex-end;
}
.container-flex-column {
  flex-direction: column;
  display: flex;
  justify-content: center;
  align-items: center;
}
@media (max-width: 668px) {
  .margin-palm {
    margin-bottom: 18px;
  }
}
@media (max-width: 668px) {
  .chips-button-container {
    flex-direction: column-reverse;
  }
  .chips-button-container .chips-container {
    margin-top: 16px;
  }
  .chips-button-container button {
    float: right;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.more-options-drop-down {
  position: absolute;
  z-index: 100;
  min-width: 320px;
  background-color: #fff;
  top: 24px;
  right: 1px;
  padding: 16px 0;
  margin-top: 2px;
  border: 1px solid #d6d6d6;
  border-radius: 4px;
  box-shadow: 0 4px 16px 0 rgba(0, 0, 0, 0.1);
}
.more-options-drop-down .entry {
  white-space: nowrap;
  text-align: left;
  width: 100%;
  padding: 8px 16px;
  margin: 0;
}
.more-options-close-icon {
  position: absolute;
  z-index: 1;
  top: 0;
  right: 0;
  font-size: 1.4rem;
  padding: 16px;
  cursor: pointer;
}
.more-option-icon {
  font-size: 2.4rem;
  vertical-align: middle;
}
.with-icon-link {
  padding-left: 0 !important;
}
.with-icon-link i::before,
.link-text i::before {
  display: inline-block;
}
@media (max-width: 668px) {
  .more-options-drop-down {
    position: fixed;
    margin: auto;
    top: 30vh;
    left: 0;
    width: 24px;
  }
  .more-options-mobile-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 2001;
    background-color: rgba(0, 0, 0, 0.5);
  }
}
</style><style type="text/css">.Accordion_button-icon-standalone__nMZW-.Accordion_disabled__wPgaF,.Accordion_button-icon-standalone__nMZW-.Accordion_disabled__wPgaF:active,.Accordion_button-icon-standalone__nMZW-.Accordion_disabled__wPgaF:focus,.Accordion_button-icon-standalone__nMZW-.Accordion_disabled__wPgaF:hover,.Accordion_button-icon-standalone__nMZW-.Accordion_disabled__wPgaF:link,.Accordion_button-icon-standalone__nMZW-.Accordion_disabled__wPgaF:visited,.Accordion_link-text__K8fay.Accordion_disabled__wPgaF,.Accordion_link-text__K8fay.Accordion_disabled__wPgaF:active,.Accordion_link-text__K8fay.Accordion_disabled__wPgaF:focus,.Accordion_link-text__K8fay.Accordion_disabled__wPgaF:hover,.Accordion_link-text__K8fay.Accordion_disabled__wPgaF:link,.Accordion_link-text__K8fay.Accordion_disabled__wPgaF:visited,a.Accordion_disabled__wPgaF,a.Accordion_disabled__wPgaF:active,a.Accordion_disabled__wPgaF:focus,a.Accordion_disabled__wPgaF:hover,a.Accordion_disabled__wPgaF:link,a.Accordion_disabled__wPgaF:visited{color:#333;cursor:default;text-decoration:none}.Accordion_clearfix-before__01fmd:before,.Accordion_clearfix__zY8Uu:after{clear:both;content:"";display:table}.Accordion_vertical-center-container__mtgNR{height:100%}.Accordion_vertical-center-container__mtgNR:after{content:"";height:100%}.Accordion_vertical-center-container__mtgNR:after,.Accordion_vertical-center__gOfU7{display:inline-block;vertical-align:middle}.Accordion_horizontal-center__fEvvd{display:block;margin:0 auto}.Accordion_cursor-pointer__yJAGq{cursor:pointer}.Accordion_height-full__g9EfN{height:100%}.Accordion_core-hide__ubd0s,[data-theme=core] .Accordion_core-hide__ubd0s{display:none}.Accordion_cosma-hide__zN-iO,[data-theme=core] .Accordion_cosma-hide__zN-iO,[data-theme=cosma] .Accordion_core-hide__ubd0s{display:initial}.Accordion_core-hide--inline__uWqpt,[data-theme=core] .Accordion_core-hide--inline__uWqpt,[data-theme=cosma] .Accordion_cosma-hide__zN-iO{display:none}.Accordion_cosma-hide--inline__-9pww,[data-theme=core] .Accordion_cosma-hide--inline__-9pww,[data-theme=cosma] .Accordion_core-hide--inline__uWqpt{display:inline}.Accordion_core-hide--block__FtHi5,[data-theme=core] .Accordion_core-hide--block__FtHi5,[data-theme=cosma] .Accordion_cosma-hide--inline__-9pww{display:none}.Accordion_cosma-hide--block__dqbDu,[data-theme=core] .Accordion_cosma-hide--block__dqbDu,[data-theme=cosma] .Accordion_core-hide--block__FtHi5{display:block}.Accordion_core-hide--inline-block__atqyV,[data-theme=core] .Accordion_core-hide--inline-block__atqyV,[data-theme=cosma] .Accordion_cosma-hide--block__dqbDu{display:none}.Accordion_cosma-hide--inline-block__IMb9S,[data-theme=core] .Accordion_cosma-hide--inline-block__IMb9S,[data-theme=cosma] .Accordion_core-hide--inline-block__atqyV{display:inline-block}.Accordion_core-hide--flex__RSlnQ,[data-theme=core] .Accordion_core-hide--flex__RSlnQ,[data-theme=cosma] .Accordion_cosma-hide--inline-block__IMb9S{display:none}.Accordion_cosma-hide--flex__W8d0Y,[data-theme=core] .Accordion_cosma-hide--flex__W8d0Y,[data-theme=cosma] .Accordion_core-hide--flex__RSlnQ{display:flex}.Accordion_core-hide--inline-flex__AY8y3,[data-theme=core] .Accordion_core-hide--inline-flex__AY8y3,[data-theme=cosma] .Accordion_cosma-hide--flex__W8d0Y{display:none}.Accordion_cosma-hide--inline-flex__KKAmO,[data-theme=core] .Accordion_cosma-hide--inline-flex__KKAmO,[data-theme=cosma] .Accordion_core-hide--inline-flex__AY8y3{display:inline-flex}[data-theme=cosma] .Accordion_cosma-hide--inline-flex__KKAmO{display:none}.Accordion_accordion__7DMqO{background:#fff;font-family:Make It Sans IS24 Web,Verdana,DejaVu Sans,Arial,Helvetica,sans-serif;font-size:1.4rem;margin:16px 0}.Accordion_accordion-icon__-kdT6{color:#333;display:inline-block;font-size:1.6rem;height:1em;position:absolute;right:8px;top:calc(50% - .5em);transform:rotate(0);transition:transform .2s ease-out;width:1em}.Accordion_accordion-icon__-kdT6.Accordion_expanded__GVHzu{transform:rotate(180deg)}.Accordion_accordion-header__syWKu{background-color:#fff;border-bottom:1px solid #eaeaea;cursor:pointer;font-weight:600;line-height:1.8rem;padding:16px 32px 16px 8px;position:relative;-webkit-user-select:none;-ms-user-select:none;user-select:none}.Accordion_accordion-header__syWKu:first-child{border-top:1px solid #eaeaea}.Accordion_accordion-header__syWKu:focus,.Accordion_accordion-header__syWKu:hover{background-color:#eaeaea}.Accordion_accordion-header__syWKu.Accordion_expanded__GVHzu:focus,.Accordion_accordion-header__syWKu.Accordion_expanded__GVHzu:hover{background:#fff}.Accordion_accordion-panel__2V8G7{max-height:0;overflow:hidden;transition:all .2s ease-out}.Accordion_accordion-panel__2V8G7>div{background:#fff;padding:8px 32px 8px 8px}.Accordion_accordion-panel__2V8G7.Accordion_expanded__GVHzu{max-height:1000px;transition:all .4s ease-out}</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.result-list-entry__waiting .font-ellipsis {
  text-overflow: clip;
}
.result-list-entry__waiting * {
  cursor: wait;
}
.result-list-entry__waiting .background-waiting {
  background-color: #e0e0e0;
}
.result-list-entry__waiting .background-waiting .waiting-text-mask {
  visibility: hidden;
}
</style><style type="text/css">.Indicator_indicator__IhewW{color:#333;display:inline-flex;font-family:Make It Sans IS24 Web,Verdana,DejaVu Sans,Arial,Helvetica,sans-serif;font-size:14px;line-height:16px;text-align:center;-webkit-user-select:none;-ms-user-select:none;user-select:none;white-space:nowrap}.Indicator_indicator__IhewW [role=button]{cursor:pointer}.Indicator_indicator__IhewW [role=button]:focus,.Indicator_indicator__IhewW [role=button]:hover{color:#333;font-weight:700}.Indicator_indicator__IhewW [role=button]:focus svg,.Indicator_indicator__IhewW [role=button]:hover svg{stroke:#333;stroke-width:2px}.Indicator_indicator__IhewW>span{display:block}.Indicator_indicator__IhewW .Indicator_fa__nBLO8,.Indicator_indicator__IhewW [class^=is24-icon-],.Indicator_indicator__IhewW [class^=s24-icons-],.Indicator_indicator__IhewW svg{color:#adadad;font-size:12px;margin-left:4px;transition:all .4s ease}.Indicator_indicator--float__0Sab7{position:relative;right:16px;top:-16px}.Indicator_indicator--label__Voulj+.Indicator_indicator--label__Voulj,.Indicator_indicator--label__Voulj+.Indicator_indicator--tag__Vfpnv,.Indicator_indicator--tag__Vfpnv+.Indicator_indicator--label__Voulj,.Indicator_indicator--tag__Vfpnv+.Indicator_indicator--tag__Vfpnv{margin-left:10px}.Indicator_indicator--dot__-iJNh,.Indicator_indicator--numeric__Zpe7j>span{background-color:#00ffd0;border-radius:14px;box-shadow:0 0 1px 1.5px #fff;font-weight:600}.Indicator_indicator--label__Voulj>span{background-color:#d9fff8;border-radius:11px;padding:4px 12px}.Indicator_indicator--brand__4p0ak>span{background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAYCAYAAABjswTDAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgpMwidZAAAF7UlEQVRYCaWXu44dRRCGu4/XF4zBXCUuEkKEiAg55x0IiIh4B/J9ClJyx6S8AiIhIAGBCQAbY8Cwu+zuGb7vn6rRASERUNo+3V1dl78u0zszh7TcvTbGG2+NsbvOeGqM/Y0xJuvlaU7/YDzBfseeefeY89/Yw1/OGL8zHo1x8fMYR/C/uhjzvT81+79pOcbnOzdx/8wYJw9mDC6ffQCIj1bnghzwl4t1HksB3TOzdr9cRm9MeAPA45xxAv9XZoF+zSCAqdwv8H840EEu8viY6O2vcKbtW/ABtmMsz7F/mfklePJJ0vLhEQtoklUBhgQpCBwFjHxBsl+I1DP5vV44m1TGrM8XODdQ7Umu1VXGGdpsupGvPflWTrvyw2AyCYzFAG8W2PG8EqWgINFGC01BJUPOOveo9XSmvDOORlUjPB1HeNVPUMpC0bcCykORdxacPgSeA36Qm8jt2+kk7Q2uS51MCkBlNV0z4q9A2CqbvAfylY8Qy3/RR2Ktmu2DvLZV88ekJDnySFiSZADaud8ZAn36Rh0cxW9+WGuJtXwNhFgnC2RgmIXOkE40rI5kz2rHIJUtuUHbxKbBKi9pH5kOMPLq+hCDc84Cu9jEOmJ0ppyTUQ0VxUBvNKyMGdAoFNDwpDg1EPeeO+MvwRSwgK7gYkd7BiUudRhJij6ePcKEzHbMMpktJYNJtJWhZNbsmCmmjQTSpC0P5TFcpyqtIBgoD5T2LbMVg78FVgEkYKuAz8t7CN+9yob7NCBbCVb6xPmQDh12iTlPNpg3kOqYHSjXHOuJbdcB78OlX0GZNUFju1si9kyYPH0yrtwgmtf8B3D7QNBsmBWoDaR0YcjkHGXP4vwAdJyXrpnaqmbWCqhZin4FkFZsnbKZTLNWNsHyD+jyIQo7gKZnjVIDCkGZzYbg2CdaFimfQHTu/E9S2IG9OGL5t2B7X6X2LBnVV62j59qW8449BeeJYF9k4wMGJaNmoQCGp1HJ6AXhJI99erj4CcJzdeVBll6KvQosGfZccMgny7aEVPdsbLUPMOr39JRFmrocBpARkbXtOvJa04hkIN6POoYXRwJCv/uW3SpnViAD62olc9qQp039RMgfSF8yyn7kyOpCG1wT7JH/JisDRrAJoxAwviv4REryfMExakmnNYfnxjMcClJbAQOoAPCs1p5FRptmWVvOjMz6LPnpO8c5YPfcBDvBmol4Xuf0o57kNb8AbHuOupR9zQWdgLCtWoIvIGzXQMteAvFH/wI9qNb0n4FVVBb+J5caJIJkViDwQywsa5cwfdYGK+PDjAvCIJVnJECvJQ3VCE+H6LVN9SIPP8FwrHy3S3pefXo5gAn+OP/GeH+VAkhlRhyYHfmASbnkMwICx5kVIGBJHXW736JDgLGlgD0qSIOUAJM+l69tkhZfgsRmsmxmefjz6plSPcmmgHHEhj8VdNyAcRJHsnXo7LlUsltmW1++esjFnhXpM9mek4j0ugG7V1a76nUlrNxjTsysXwNpaJ9EMwblwVKZEQdGL8kjgM58KmNAtlIBUywXPToB5F7HBlmAtZMAtC9fQJ5hq4POrE1o+c5fI3rARpBE1K9om2Ard7SIxYkAHV7Y9nL3qXICkScAnWlbUPACytJK8FIt/SJje+Rcfc9NEJ9Qqfp9GYLlGyrRlaNkKNIIVhBmMA7hz7rAc9VUv2kqPa+eMvAD2AMApzqADyhtQVsbwU/GK7CAE4sPl0GzXvi+WxuZ76Nc0DjRVxvJfefDIF/QkgIOycyaDc4MMIDgZdZx8RTNOgvOtRVHTNqohGQuWxEVsIHxLbf7SQ6b8y9oue9Zv8rQCAbS9ESzfMqe/x62imXx466/eicvQMObxA/C15kFyj7vGfL9yGNK+cmSV1wCw2cHmBZSiBFZffvlzH8tQS7fMr6ko+6xN8XQ8vn7/LwLmI+Zf6QN6StSP9/+Juf/9ZN34mNsvQmQV8j2LR7aM26Zq+z9rPerVZsprR+VfFrvALR/uJ6lP00GQE3MGfN1+vXOCQiNIvQXYk3fyxwXPjAAAAAASUVORK5CYII=") no-repeat 50% 50%;background-size:100% 100%;border-radius:0;font-weight:600;padding:4px 8px;text-transform:uppercase}.Indicator_indicator--plus__m6eYC>span{position:relative}.Indicator_indicator--plus__m6eYC>span:before{background:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkiIGhlaWdodD0iOSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTQ3LjgyNiA0LjY5OGExLjEyIDEuMTIgMCAwIDEtLjQuNTEyYy4wNDcuMDg4LjEwMy4xODYuMTQ4LjI4NS4wMDYuMDE0LS4wNC4wMzUtLjA1Ny4wNTRhLjM2Mi4zNjIgMCAwIDAtLjA5My4xMzhjLS4yMjIuMTIxLS40OTQuMTg3LS44MTYuMTI5YS4yNjEuMjYxIDAgMCAwLS4xMDQuMDAzYy0uMzkuMTI2LS44MTguMTA3LTEuMjI2LjEyOC0xLjY5NC4wODgtMy4zODcuMTY1LTUuMDguMjQtMS4yNTguMDU3LTIuNTE3LjExLTMuNzc1LjE1MS0uNTMxLjAxOC0xLjA2LS4wMDctMS41OS4wMS0uNTEuMDE2LTEuMDI1LjA3My0xLjUzNi4wOS0uNTg4LjAyLTEuMTg1LjA3NS0xLjc2MS4wMS0uMTU3LS4wMTgtLjM1Mi4wMTctLjUyOS4wMzMtLjIxMS4wMi0uNDIzLjA1NS0uNjMzLjA2NC0uNzk2LjAzMi0xLjU5My4wNjItMi4zODkuMDgyLTEuMjEzLjAzLTIuNDI2LjExLTMuNjM5LjE2Ni0uODEuMDM3LTEuNjIuMDctMi40My4xMTQtMS43NzcuMDk0LTMuNTUzLjE5LTUuMzI5LjI5My0xLjc4Ni4xMDQtMy41NzMuMjE5LTUuMzYuMzI5LS40OTYuMDMtLjk4My4wNjItMS40NzUuMTU4LS4zMjUuMDYzLS43LjA0Ni0xLjA1My4wNjNsLTEuNzEuMDhjLS41Mi4wMjQtMS4wNDcuMDIzLTEuNTYxLjA3Ny0uODEzLjA4Ny0xLjYxNS4wOC0yLjQxOC4xLS41Ny4wMTMtMS4xNzIuMDMzLTEuNjc0LS4xMDYtLjE1OS0uMDQ0LS4zMi0uMTEtLjQtLjE4OC0uMjgtLjI3OC0uNTA2LS41Ny0uNTkzLS44ODctLjA0OS0uMTc4LS4wMDktLjM2OC4wMDUtLjU1My4wMTMtLjE4OC4wNDctLjM3Ni4wNjQtLjU2NS4wMTMtLjE0OC4wMjUtLjI5Ny4wMTktLjQ0NC0uMDA1LS4xMDcuMDExLS4yMjQtLjE5Ni0uMjY1LjA1Mi0uMDkuMTI3LS4xNjguMTQtLjI0NS4wNTYtLjMzOS4xMDQtLjY3OC4xMzMtMS4wMTYuMDEtLjEyNC0uMDY5LS4yNDQtLjA2LS4zNjguMDItLjMwMy0uMTA3LS41OTcuMDQ5LS45MS4wNTUtLjExLjA1Ny0uMjIyLjI5OC0uMzMzLjM1NC4wMDUuODEuMDY0IDEuMjIuMDA0LjUzMi0uMDc3IDEuMDMzLS4wNTYgMS41NDYtLjA3NyAxLjY5My0uMDY5IDMuMzg1LS4xMTkgNS4wNzgtLjE5MSAxLjAyNS0uMDQ0IDIuMDUxLS4xMiAzLjA3Ni0uMTc1IDEuMjAzLS4wNjUgMi40MDYtLjEyIDMuNjA5LS4xODcgMS4yODYtLjA3MSAyLjU3MS0uMTU1IDMuODU2LS4yMjguOTktLjA1NiAxLjk3OC0uMTAzIDIuOTY2LS4xNTYgMS4yODctLjA2OCAyLjU3My0uMTQ0IDMuODYtLjIwMy45ODctLjA0NSAxLjk3My0uMDY0IDIuOTYtLjEgMS4wODItLjA0IDIuMTY1LS4wODYgMy4yNDctLjEyNiAxLjI2LS4wNDUgMi41Mi0uMDgyIDMuNzgtLjEzQzM3LjI3LjUwOSAzOC41NDUuNDUyIDM5LjgyLjM5OGMxLjA5Ny0uMDQ2IDIuMTkzLS4wODkgMy4yOS0uMTQuODkzLS4wNDIgMS43ODctLjA5MyAyLjY4LS4xNDQuMzY4LS4wMi43NS0uMDIxIDEuMDk4LS4wODMuMjQ3LS4wNDQuNDMxLS4wMy42NC0uMDEuMTQuMDE0LjIxMi4wNTUuMTM3LjEyMy0uMTY1LjE1MS4wMDMuMjUuMTUuMzc2bC0uNDcyLjIxNC40MzktLjAzMS0uMTEzLjUyMWMuMDEyLjAwNi4wNDguMDI4LjA5NS4wNDEuMjAzLjA1OC4yMDIuMTQuMTA2LjI0NS0uMDUzLjA1OS0uMDU3LjEyNi0uMDkzLjIxMmwtLjI2MS4wNy4wMDguMDQ4aC4zODNsLS4wMDctLjAwNGMuMDk4LjA5Ni4zNDYuMTczLjEwMy4zMTNsLjAwNS0uMDAzYy0uMDYuMTE0LS4xMzcuMjMuMDM0LjMxMS0uMDg2LjA4LS4yOC4yLS4yMzUuMjMuMjE2LjE1LjAwNS4zMjIuMDYuNDc2LjAzMi4wODcuMDExLjE4NC0uMDIyLjI3NS0uMDMxLjA4NS4wMDMuMTMxLjI2LjEyMy0uMzE1LjEyLS4zNjUuMjMtLjI3My4zNjguMDUxLjA3OC4wMDYuMTcuMDc3LjI1OC4wNTQuMDY5LS4wODIuMTc3LS4xLjI2OC0uMDE1LjA4Mi4wMTYuMTY0LjAyNy4yNDZsLS4wMS0uMDAzWm0tMTEuNjQzLTIuMjR2LS4wNTZsLS45OTUuMDctLjAwMi4wMS45OTctLjAyM1ptLTEwLjk5OS0uMDAzLS4wMDEtLjA1LS45OTUuMDcxLS4wMDIuMDE3Ljk5OC0uMDM4Wm05LjAwMy4wMTEtLjAwOC0uMDUtLjk5Mi4wNXYuMDVsMS0uMDVabS04LjAwOC4wMDcuMDA1LS4wNDNhMi45NjkgMi45NjkgMCAwIDAtLjk5Ny4wNzJsLjk5Mi0uMDNabTYuMDEzLS4wMDQtLjAwNS4wMzQuOTk1LS4wNC4wMDItLjAzNi0uOTkyLjA0MlptLTEuMDA3LjAwNi4wMDUuMDUyLjk5Ni0uMDd2LS4wMDlsLTEgLjAyN1ptLTEwLjk5My4wMS0uMDA0LjAzMi45OTctLjA3LS4wMDItLjAzMi0uOTkxLjA3Wm0yMS4yMDctLjAxNy0uMDAxLS4wMzUtLjQyNy4wMy4wMDUuMDM1LjQyMy0uMDNabS0xOS4yMTQtLjAzMS0uMDAzLS4wMTMtLjk5NS4wN2MwIC4wMDUgMCAuMDA5LjAwMi4wMTNsLjk5Ni0uMDdabS0uMTc3LjAyMXYuMDI5bC4zNTQtLjAxNHYtLjA0bC0uMzU0LjAyNVptLS45NDgtLjAwMi0uMDA1LjAzNy4yNjQtLjAxOC0uMDA5LS4wMy0uMjUuMDExWm0yNS4xNTUgMi45Ni0uMDgxLjAwOC4wNC4wOS4wNjMtLjAwOWE5LjM2NiA5LjM2NiAwIDAgMS0uMDIyLS4wODlaTTMyLjAwMyAxLjQ2MWwuMDA5LjAzNS4zNTUtLjAyNnYtLjAyM2wtLjM2NC4wMTRaTTE4LjA5NyAxLjQ1bC0uMDA0LjA0NC4xODQtLjAxNy4wMDItLjAyN2gtLjE4MlptMjguMTI3IDMuMDE3Yy0uMDA3LS4wMDYtLjAxNy0uMDItLjAyMy0uMDE4LS4wMTkuMDAxLS4wMzYuMDA5LS4wNTQuMDE0LjAwOC4wMDcuMDE4LjAyLjAyNS4wMi4wMTgtLjAwMi4wMzUtLjAxLjA1My0uMDE2Wm0tMjIuMTA2LTIuMDEuMDAxLjAyNy4xMzQtLjAxNy0uMDAzLS4wMTYtLjEzMi4wMDVabS0uOTg0LjAwOWMuMDQ0LjAwNS4wNjMuMDEuMDgxLjAwOC4wMDgtLjAwMS4wMTUtLjAxNS4wMjEtLjAyMmwtLjEwMi4wMTRabTIzLjA3My4wMDMtLjAwMi0uMDE0LS4wNC4wMWMuMDA1LjAwNC4wMS4wMS4wMTcuMDEuMDA3IDAgLjAxNy0uMDA0LjAyNS0uMDA2Wk0yNy4xMyAyLjQ2NWMuMDQ4LjAwNy4wNy4wMTIuMDg5LjAxLjAwOSAwIC4wMTUtLjAxNi4wMjMtLjAyNmwtLjExMi4wMTZabTEuMDUxLjAyLjA1OC0uMDE4Yy0uMDEtLjAwOC0uMDIzLS4wMjItLjAyOC0uMDIxLS4wMjcuMDA1LS4wNS4wMTMtLjA3Ni4wMmwuMDQ2LjAxOFptLTIuOTY4LS4wMTEuMDA2LS4wMTdoLS4wNmwtLjAwNS4wMTZoLjA1OVptMS4wMjUtLjAyNWMtLjAzLS4wMDItLjA1OC0uMDA1LS4wODYtLjAwMy0uMDA3IDAtLjAyMS4wMjUtLjAxNy4wMjcuMDI1LjAwNi4wNTQuMDA5LjA4Mi4wMTJsLjAyLS4wMzZabS0zLjAzNC4wMzQuMDI1LS4wMjljLS4wMi0uMDAyLS4wNDItLjAwOC0uMDYtLjAwNS0uMDEyLjAwMi0uMDE3LjAxNy0uMDI1LjAyNmwuMDYuMDA4Wm0xNy4wMjMtLjAyOGMtLjAxOS0uMDAyLS4wNDItLjAwOS0uMDU2LS4wMDUtLjAxMy4wMDMtLjAxNy4wMTctLjAyNS4wMjYuMDE4LjAwMy4wNDIuMDEuMDUzLjAwNi4wMTUtLjAwNS4wMi0uMDE4LjAyOC0uMDI3Wm01Ljk4OS0uOTg5LS4wNDItLjAxNGMtLjAwNi4wMDQtLjAxOC4wMTItLjAxNy4wMTNsLjA0LjAxNS4wMTktLjAxNFpNMjAuMjEzIDIuNDc1Yy0uMDA3LS4wMDgtLjAxMy0uMDE2LS4wMjItLjAyM2EuMDcuMDcgMCAwIDAtLjAyNy4wMDRjLS4wMDQuMDA4LS4wMDMuMDE3LS4wMDQuMDI2bC4wNTMtLjAwN1ptMTUuMDM3LTFjLS4wMTctLjAxNC0uMDI2LS4wMy0uMDM2LS4wMy0uMDMuMDAyLS4wNjEuMDEtLjA5Mi4wMTYuMDEuMDA4LjAxOS4wMjQuMDMyLjAyNC4wMjkuMDAxLjA2LS4wMDUuMDk2LS4wMVptMTAuOTY1IDEuOTg5LS4wNDQtLjAxMmMtLjAwNS4wMDUtLjAxNi4wMTQtLjAxNC4wMTQuMDE0LjAwNS4wMy4wMDkuMDQ2LjAxM2wuMDEyLS4wMTVabS45NTYgMS45OTMuMDIyLjAxN2MuMDAyLS4wMDQuMDA5LS4wMS4wMDYtLjAxMS0uMDA0LS4wMDMtLjAxNS0uMDAzLS4wMjgtLjAwNlpNMzkuMTc1IDIuNDZsLS4wMS4wMWMuMDEgMCAuMDIzLjAwNC4wMjYuMDAzLjAwNy0uMDA0LjAxLS4wMS4wMTQtLjAxNWwtLjAzLjAwMlptNy4wMi0uMDA3Yy0uMDA5IDAtLjAyNi4wMDMtLjAyNi4wMDMgMCAuMDA4LjAwMy4wMTYuMDA2LjAyNWwuMDI3LS4wMDVjMC0uMDA4LS4wMDQtLjAxNi0uMDA3LS4wMjNabS0xNy4wMTIuMDAzYy0uMDA4LjAwNC0uMDIxLjAwNy0uMDI0LjAxLS4wMDIuMDA0LjAxLjAwOC4wMTUuMDEybC4wMzgtLjAxNy0uMDI5LS4wMDVaIiBmaWxsPSIjMDBGRkQwIi8+PC9zdmc+") no-repeat 0 50%;background-size:contain;content:"";height:30%;left:0;position:absolute;top:85%;width:60%}.Indicator_indicator--plus__m6eYC>span:after{background:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik05LjI0IDIzLjg5OGMuMDQ2LjAxMy4xMDMuMDMuMTc4LjA1bC4xMDUuMDE1Yy4xMTguMDE3LjI4NC4wNDIuNDU1LjAzNi4zNDgtLjAxNC43MDMtLjA4OCAxLjA1OC0uMTYzLjQzOC0uMDkzLjg3Ny0uMTg2IDEuMzAzLS4xNjJhLjE0NC4xNDQgMCAwIDAgLjA4LS4wMjdjLjI4Ny0uMTg1LjU3LS4yNDMuODU1LS4zLjE4Ny0uMDM5LjM3NC0uMDc3LjU2Mi0uMTUxLjE1NS0uMDYyLjMxLS4xMS40NjYtLjE2LjExLS4wMzUuMjIyLS4wNy4zMzMtLjExLjEwNi0uMDM4LjIxMy0uMDkyLjMxOC0uMTU1LjI3MS0uMTY0LjQzNS0uNDQ2LjQ2Ni0uODQuMDItLjI1Mi4wMjItLjUwMi4wMjQtLjc1MWwuMDAxLS4xNjdjLjAwNS0uMzk1LjAwNS0uNzg4LjAwNS0xLjE4MSAwLS44MjctLjAwMS0xLjY1NC4wNDQtMi40OTIuMDY0LTEuMjA2LjE0NC0yLjQxNS4yMzgtMy42MjZhNjQuMzA4IDY0LjMwOCAwIDAgMSAxLjEtLjAyM2MuMzI0LS4wMDUuNjQ2LS4wMTIuOTY5LS4wMThhMTEyLjA1IDExMi4wNSAwIDAgMSAxLjk4NS0uMDI5YzEuMTg4LS4wMDIgMi4zNzguMDEyIDMuNTY5LjAyN2guMDMzYy4zNzMuMDA1Ljc0OC4wMTcgMS4xMjMuMDI5bC42ODIuMDJjLjE4Mi4wMDUuMzU2LS4wMTYuNDU4LS4xMDYuMjUtLjIyLjM3OS0uNDguMzM2LS43NWwtLjAxOC0uMTFhMjAuNzggMjAuNzggMCAwIDAtLjMwNC0xLjYzIDUuNTU1IDUuNTU1IDAgMCAwLS4wNy0uMjUxYy0uMDY2LS4yMy0uMTMzLS40Ni0uMTEzLS42ODEuMDE2LS4xNzgtLjAyNC0uMzU0LS4wNjQtLjUyOS0uMDMxLS4xMzQtLjA2Mi0uMjY5LS4wNjctLjQwNC0uMDA3LS4xODctLjEyMS0uMzcyLS4zMTUtLjUzOGE4LjcxMyA4LjcxMyAwIDAgMS0uMTExLS4wM2MtLjE5LS4wNTMtLjM3LS4xMDMtLjYtLjA5My0uMzg4LjAxNy0uNzgxLjAxNi0xLjE3NC4wMTUtLjIwNyAwLS40MTMtLjAwMS0uNjIuMDAxbC0uMzI2LjAwM2MtLjQ5LjAwNC0uOTguMDA4LTEuNDYzLjAzMi0uMDc4LjAwMy0uMTUuMDItLjIyNS4wMzdhMS4wNDEgMS4wNDEgMCAwIDEtLjM2NS4wMzdsLS4wMzItLjAwM2MtLjM3LS4wNC0uNzQ1LS4wODItMS4wNzEuMDQ0bC0uODEzLjAwNmMtLjY0LjAwNS0xLjI3OC4wMS0xLjkxNy4wMTNoLS4xNGMuMDY4LS42NTguMTM4LTEuMzE4LjIxMS0xLjk3OGwuMDQtLjM1MWMuMTgtMS42NDguMzYxLTMuMjkuNzcyLTQuOTQ4LjE3My0uNjk3LjAzLTEuMDg2LS4zNzItMS4zNGEuNzc4Ljc3OCAwIDAgMC0uMzg1LS4xNGMtLjQ3Mi0uMDMxLS45NDktLjA2NC0xLjQ0My4wOTEtLjQuMTI1LS43OC4xODYtMS4xNzIuMjEtLjUyLjAzMy0xLjAzMy4wNjEtMS41NC4wMDgtLjUwMi0uMDUyLTEuMDMtLjAxNy0xLjU3Mi4yOS0uMjguMTU3LS40OTMuNDE2LS42Ny44MDItLjI1NC41NDgtLjI5OSAxLjEtLjI2NCAxLjYxMi4wMzIuNDc4LS4wMDIuOTYyLS4wMzcgMS40NTNsLS4wMS4xNTVjLS4wMTcuMjMxLS4wMzcuNDY1LS4wNTcuNjk4LS4wNTguNjY0LS4xMTUgMS4zMjktLjA3OCAxLjk2OS4wMTEuMTgzLS4wMDguMzgzLS4wMjcuNThsLS4wMS4xMTYtLjA4OC45NzZjLS4xMS4wMTgtLjIxNC4wNTEtLjMxLjFhLjg3Ljg3IDAgMCAwLS40ODctLjA5IDYuNjQzIDYuNjQzIDAgMCAxLS44NTcuMDI4bC0uMjkyLS4wMDJhMzkuODMgMzkuODMgMCAwIDAtMS45NjQuMDc0bC0uMTIuMDA2Yy0uMDg0LjAwNS0uMTYuMDM3LS4yMzYuMDdhMS45NCAxLjk0IDAgMCAxLS4wODMuMDM0Yy0uNjQtLjE3LTEuMjM1LS4wOTktMS44NzktLjAyMWwtLjAyNC4wMDMuMTcuMDk1LjIzNS4xMzJhNTI2LjYxNSA1MjYuNjE1IDAgMCAwLS42NS4wMTJsLjE1Ny4xNjVjLS42MzcuMDg4LTEuMjc3LjA4NC0xLjkxNi4wOC0uMzI2LS4wMDEtLjY1Mi0uMDAzLS45NzYuMDA3LS4wMjguMDUtLjA2NS4xLS4xLjE0OC0uMDguMTA2LS4xNTYuMjEtLjEzNS4zMS4wMjcuMTI3LjAyLjI0OS4wMTQuMzctLjAwNi4xMDUtLjAxMS4yMDkuMDA0LjMxMy4xMDcuNzUxLjIyIDEuNTAzLjM2NyAyLjI1NS4wNTIuMjY5LjE4LjU0LjMxNy44MDUuMTU3LjMuNTU4LjQ2NiAxLjA2NS40NjQuMzUyLS4wMDIuNzAzLS4wMTEgMS4wNS0uMDI5IDEuMzEyLS4wNjUgMi42MjItLjEzMyAzLjkzMy0uMmwxLjI4Ni0uMDY3Ljg3Ny0uMDQ0LjA5NS0uMDA1YTExNy4zMTcgMTE3LjMxNyAwIDAgMC0uMzY2IDkuMDJjLS4wMDIuNDc2LjEzNC43NS40MzMuODM0bC4xNTYuMDQ1Wk0zLjYzIDkuNDE1bC4wMTYuMDA5LjAyNC0uMDFoLS4wNFptMS41MzktLjE5NGExMy40MTggMTMuNDE4IDAgMCAwLS4wNjYtLjAwNi44NDYuODQ2IDAgMCAwIC4wMjUtLjAwOGwuMDQxLjAxNFptMCAwIC4wMjMuMDAyYy4wNjcuMDA2LjEzNS4wMTIuMjAyLjAxNi4wOTYuMDA2LjEzLjAyOC4wODcuMDY0LS4wMDkuMDA3LS4wNjQuMDAxLS4wOTEtLjAwNy0uMDY0LS4wMi0uMTI2LS4wNDItLjE4OC0uMDY0bC0uMDMzLS4wMTFabS0uMzcyLjE2MS0uMTEuMDE2LjAwNS0uMDUuMTA1LjAzNFptNC4zOC0uMjkxYS45NDkuOTQ5IDAgMCAwLS4wMS0uMDA2IDEuMTIzIDEuMTIzIDAgMCAwLS4wMTEuMDA2bC4yMTIuMDItLjE5LS4wMloiIGZpbGw9IiMwMEZGRDAiLz48L3N2Zz4=") no-repeat 0 50%;background-size:contain;content:"";height:60%;position:absolute;right:-28%;top:-5%;width:35%}.Indicator_indicator--tag__Vfpnv>span{background-color:#eaeaea;border-radius:5px;color:#333;padding:4px 12px}.Indicator_indicator--dot__-iJNh{height:0;padding:6px;width:0}.Indicator_indicator--dot__-iJNh.Indicator_indicator--float__0Sab7{right:6px;top:-18px}.Indicator_indicator--numeric__Zpe7j>span{border-radius:100%;height:24px;padding:4px 0;width:24px}.Indicator_indicator--numeric__Zpe7j.Indicator_indicator--expanded__1n-B5>span{border-radius:12px;padding:4px 6px;width:auto}</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.oval-button-mobile {
  width: 327px;
}
.oval-button {
  width: 250px;
}
.teaser-flex-container {
  flex-direction: column;
  align-items: center;
}
@media (max-width: 1013px) {
  .teaser-section {
    min-height: 340px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
.bullet-container {
  max-width: 218px;
}
@media (max-width: 1013px) {
  .bullet-container {
    max-width: 243px;
  }
}
.teaser-powered-by {
  font-size: 1rem !important;
  line-height: 2.2rem !important;
}
.teaser-powered-by-container {
  flex-direction: row;
  align-items: center;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.teaser-flex-container {
  flex-direction: column;
  align-items: center;
}
@media (max-width: 1013px) {
  .teaser-section {
    min-height: 340px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
.teaser-section .teaser-input,
.teaser-section .teaser-button {
  width: 220px;
}
.input-hint {
  font-size: 16px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
@media (max-width: 668px) {
  .is24-palm-center {
    text-align: center;
  }
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.map-flyout__message--boxed {
  width: 215px;
}
</style><style>/* doiuse-disable multicolumn */
/* doiuse-enable multicolumn */
/* Primary */
/* Dark Mode */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.map-flyout-container {
  position: fixed;
  z-index: 11730001;
  left: 0;
  right: 0;
  top: 0;
}
.map-flyout-container {
  visibility: hidden;
  transform: translateY(-100%);
  transition: visibility 250ms ease-in, transform 250ms ease-in;
}
.map-flyout-container--open {
  visibility: visible;
  transform: translateY(0);
}
.map-flyout-container {
  height: 60%;
}
.map-flyout-container .page-wrapper {
  background-color: transparent;
}
.map-flyout-area {
  background-color: #fafafa;
}
@media (min-width: 669px) {
  .map-flyout-area {
    padding: 24px;
  }
}
.map-flyout-area .map-flyout__map-container {
  background-color: #e0e0e0;
  border: 1px solid #d4d4d4;
}
@media (max-width: 668px) {
  .map-flyout__close-icon {
    margin-top: 16px;
    margin-right: 16px;
  }
}
@media (min-width: 669px) {
  .map-flyout__close-icon {
    margin-top: 8px;
    margin-right: 8px;
  }
}
</style><script type="module" src="https://app.usercentrics.eu/browser-ui/3.32.0/index.module.js"></script><style>.touchpoint-brandBar__bar--3Y_Jm {
  width: 100%;
  height: 16px;
  background: #343434;
}
</style><style>/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.touchpoint-profileImage__container--1Hd8p {
  width: 142px;
  position: relative;
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-profileImage__container--1Hd8p {
    width: 188px;
  }
}
@media (min-width: 1014px) {
  .touchpoint-profileImage__container--1Hd8p {
    width: 202px;
  }
}
@media all and (min-width: 1163px) {
  .touchpoint-profileImage__container--1Hd8p {
    width: 100%;
  }
}
.touchpoint-profileImage__container--1Hd8p.touchpoint-profileImage__containerAtlas--3_qkQ {
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.21);
  width: 200px !important;
  height: 200px !important;
  overflow: hidden;
}
@media (min-width: 1014px) {
  .touchpoint-profileImage__container--1Hd8p.touchpoint-profileImage__containerAtlas--3_qkQ {
    width: 240px !important;
    height: 240px !important;
  }
}
.touchpoint-profileImage__touchpointBadgeAtlas--38DlE {
  position: relative;
  top: -24px;
}
@media (max-width: 668px) {
  .touchpoint-profileImage__touchpointBadgeAtlas--38DlE {
    top: -19px;
  }
}
.touchpoint-profileImage__touchpointBadgeAtlas--38DlE.touchpoint-profileImage__mapView--1B8g8 {
  top: -19px;
}
.touchpoint-profileImage__touchpointBadgeAtlas_immoExpert--22Iqn {
  position: relative;
  top: -28px;
}
@media (max-width: 668px) {
  .touchpoint-profileImage__touchpointBadgeAtlas_immoExpert--22Iqn {
    top: -22px;
  }
}
.touchpoint-profileImage__touchpointBadgeAtlas_immoExpert--22Iqn.touchpoint-profileImage__mapView--1B8g8 {
  top: -22px;
}
.touchpoint-profileImage__touchpointBadgeStandard--3XSBz {
  position: absolute;
  right: 0;
  bottom: 8px;
  width: 75.5%;
}
.touchpoint-profileImage__touchpointBadgeStandard_immoExpert--2S4dM {
  background: #00FFD0;
}
.touchpoint-profileImage__touchpointPictureContainer--fxL6y {
  position: relative;
  overflow: hidden;
}
.touchpoint-profileImage__link--1d5bW {
  outline: 0;
}
.touchpoint-profileImage__image--1iA0M {
  max-width: 100%;
  vertical-align: top;
}
.touchpoint-profileImage__imageCircle--3i2S5 {
  max-width: 100%;
  vertical-align: top;
  border-radius: 100%;
}
.touchpoint-profileImage__withStyleBorder--2fR1t {
  border: 3px solid #FFFFFF;
  filter: drop-shadow(0px 2px 5px rgba(0, 0, 0, 0.457031));
  width: 100%;
}
.touchpoint-profileImage__touchpointRoundPictureContainer--2viwY {
  position: relative;
  overflow: hidden;
  border-radius: 100%;
  margin-top: 16px;
}
@media (max-width: 668px) {
  .touchpoint-profileImage__touchpointRoundPictureContainer--2viwY {
    width: 120px;
    height: 120px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-profileImage__touchpointRoundPictureContainer--2viwY {
    height: 184px;
    width: 184px;
  }
}
</style><style>/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
@media (max-width: 668px) {
  .touchpoint-companyLogo__logo--2scoq {
    max-width: 120px;
    max-height: 32px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-companyLogo__logo--2scoq {
    max-width: 150px;
    max-height: 40px;
  }
}
@media (min-width: 1014px) {
  .touchpoint-companyLogo__logo--2scoq {
    max-width: 100%;
    max-height: 50px;
  }
}
@media (max-width: 668px) {
  .touchpoint-companyLogo__logoAtlas--1ZAhl {
    max-width: 96px;
    max-height: 40px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-companyLogo__logoAtlas--1ZAhl {
    max-width: 180px;
    max-height: 48px;
  }
}
@media (min-width: 1014px) {
  .touchpoint-companyLogo__logoAtlas--1ZAhl {
    max-width: 180px;
    max-height: 48px;
  }
}
.touchpoint-companyLogo__logo--2scoq.touchpoint-companyLogo__logoMapView--1m4kf {
  max-width: 96px;
  max-height: 40px;
}
</style><style>/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 {
    width: 100%;
    position: relative;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 {
    width: 100%;
  }
}
@media (min-width: 1014px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 {
    max-width: 202px;
  }
}
@media all and (min-width: 1163px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 {
    max-width: 252px;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointTitle--3ehZz {
  padding-bottom: 4px !important;
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointTitle--3ehZz {
    color: #333 !important;
  }
}
@media (min-width: 669px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointTitle--3ehZz {
    font-size: 1.8rem !important;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointTitle--3ehZz {
    font-weight: 600;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointSeparator--1PVbt {
  margin-bottom: 8px;
  margin-top: 8px;
  border-top: 1px solid #e0e0e0;
  position: relative;
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointSeparator--1PVbt::after {
  content: "";
  display: block;
  border-right: 1px solid #e0e0e0;
  border-bottom: 1px solid #e0e0e0;
  border-top: 1px solid transparent;
  border-left: 1px solid transparent;
  top: -7px;
  left: 27px;
  height: 13px;
  width: 13px;
  background-color: #fff;
  position: absolute;
  transform: rotate(45deg);
}
@media (min-width: 1014px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointSeparator--1PVbt {
    margin-bottom: 16px;
  }
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointSeparator--1PVbt::after {
    background-color: #fafafa;
  }
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorPicture--1WVCE {
    padding-top: 16px;
    padding-right: 16px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorPicture--1WVCE {
    width: 212px !important;
    flex: 0 1 auto !important;
  }
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointMiddleSection--1yBYg {
    padding: 16px 16px 0 16px;
    flex: 0 1 auto !important;
    width: calc(100% - 158px) !important;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointMiddleSection--1yBYg {
    flex: 1 1 auto !important;
    padding-top: 24px;
    padding-right: 8px;
    width: calc(100% - 150px - 212px) !important;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorName--7d2FC {
  color: #343434;
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorName--7d2FC a {
  color: #343434 !important;
  text-decoration: none;
  font-weight: 600 !important;
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorName--7d2FC {
    color: #333 !important;
    padding-top: 8px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorName--7d2FC {
    padding-top: 8px;
  }
}
@media (min-width: 669px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorName--7d2FC {
    font-size: 1.4rem !important;
    font-weight: 600 !important;
  }
}
@media (min-width: 1014px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRealtorName--7d2FC {
    padding-top: 16px;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRating--1j3dL {
  padding-top: 4px;
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRating--1j3dL .touchpoint-touchpoint__touchpointRatingCount--1Eaww {
  position: relative;
  top: 1px;
  left: 4px;
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRating--1j3dL .touchpoint-touchpoint__touchpointRatingCount--1Eaww {
    font-size: 1.2rem !important;
  }
}
@media (min-width: 1014px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointRating--1j3dL {
    padding-top: 8px;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointPictureContainer--2ep8v {
  position: relative;
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointPictureContainer--2ep8v {
    width: 188px;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBadge--1LgcK {
  position: absolute;
  right: 0;
  bottom: 7px;
  width: 100%;
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBadge--1LgcK {
    bottom: 3px;
  }
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q {
    padding: 16px;
  }
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q .touchpoint-touchpoint__touchpointButtonContainer--2zpEe {
    text-align: right;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q {
    padding-top: 24px;
    width: 150px !important;
    flex: 0 1 auto !important;
    display: flex !important;
  }
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q > div > div {
    text-align: right !important;
  }
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q .touchpoint-touchpoint__touchpointButtonContainer--2zpEe {
    align-self: flex-end;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q .touchpoint-touchpoint__touchpointButton--p4y1O {
  padding-left: 0;
  padding-right: 0;
}
@media (max-width: 668px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q .touchpoint-touchpoint__touchpointButton--p4y1O {
    width: 142px !important;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q .touchpoint-touchpoint__touchpointButton--p4y1O {
    width: 150px !important;
  }
}
@media (min-width: 1014px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q .touchpoint-touchpoint__touchpointButton--p4y1O {
    margin-top: 16px;
  }
}
@media (min-width: 1014px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointBottomSection--2Qt_q {
    padding-top: 16px;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointTitleDescription--1ufc_ {
  color: #747474;
  letter-spacing: normal;
  font-size: 13px;
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointTitleDescription--1ufc_ {
    text-align: left;
  }
}
.touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointDescriptionLink--1w3zj {
  font-size: 13px;
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-touchpoint__touchpoint--1wqE6 .touchpoint-touchpoint__touchpointDescriptionLink--1w3zj {
    text-align: left;
    font-size: 12px;
  }
}
.touchpoint-touchpoint__demoSaleBadge--v_w5r {
  background: red;
  font-size: 18px;
  color: white;
  font-weight: bold;
  text-align: center;
}
@media (min-width: 1014px) {
  .touchpoint-touchpoint__demoSaleBadge--v_w5r {
    position: relative;
    max-width: 252px;
    padding-top: 0 !important;
  }
}
</style><style>/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
/* Primary */
.touchpoint-badge__touchpointBadgeImage--3VUV8 {
  display: block;
}
@media (max-width: 668px) {
  .touchpoint-badge__touchpointBadgeImage--3VUV8 {
    height: 21px;
  }
}
.touchpoint-badge__touchpointBadgeImage_Atlas--2JMEB {
  width: 100%;
  display: block;
}
.touchpoint-badge__touchpointCenteredBadgeImage--3WyG8 {
  width: 100%;
  display: block;
  position: absolute;
}
@media (min-width: 1014px) {
  .touchpoint-badge__touchpointCenteredBadgeImage--3WyG8 {
    height: 32px;
    right: 30.5px;
    bottom: -23px;
  }
}
@media (max-width: 668px) {
  .touchpoint-badge__touchpointCenteredBadgeImage--3WyG8 {
    height: 16px;
    right: 17.5px;
    bottom: -15px;
  }
}
@media (min-width: 669px) and (max-width: 1013px) {
  .touchpoint-badge__touchpointCenteredBadgeImage--3WyG8 {
    height: 24px;
    right: 23px;
    bottom: -20px;
  }
}
</style></head>



  
  
    
  







<body id="is24-de" class="LIVING fullsize-map" data-theme="cosma" data-usewebp="true" style="--viewport-height: 823px;">

  <div class="viewport">
    










<div class="page-wrapper page-wrapper--full-width absolute-position">
  
    <div class="content-wrapper">
      <div class="content-wrapper--negate-padding">
        






<script src="//tags-eu.tiqcdn.com/utag/immobilienscout/is24/prod/utag.js" type="text/javascript" async=""></script><script>
    (function () {
        var styles = document.getElementById("topnavigation__style-element");
        styles.removeAttribute("scoped");
        document.getElementsByTagName("head")[0].appendChild(styles);
    }());
</script>
<header class="page-header content-wrapper align-middle header-desk-padding-vertical-s padding-horizontal-l" role="banner" data-path="default-2023">
  <div class="noselect only-desk-and-up-content-wrapper grid grid-flex grid-align-center grid-fill-rows">
    <div class="grid-item grid-align-center grid-item-fixed-width header-desk-padding-vertical-m header-lap-padding-vertical-l header-palm-padding-vertical-l">
  <div class="page-header__content page-header__logo-container desk-line-height-18 lap-line-height-0 palm-line-height-0">
    <a class="page-header__logo" title="ImmoScout24" aria-label="ImmoScout24" href="//www.immobilienscout24.de/"><img class="desk-height-28 lap-height-28 palm-height-l" alt="ImmoScout24" src="//www.immobilienscout24.de/etc/designs/is24/img/immoscout24.svg">
    </a></div>
</div>
<div class="grid-item grid-item-fixed-width palm-hide lap-hide padding-vertical-m margin-left-xxl">
  <div class="link-container padding-top-s padding-bottom-xs">
    <a class="page-header__link link line-height-l" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;header&quot;,&quot;evt_ga_label&quot;:&quot;click_fuersuchende&quot;}" href="//www.immobilienscout24.de/suchende.html">Für Suchende</a>
  </div>
</div>

<div class="grid-item grid-item-fixed-width palm-hide lap-hide padding-vertical-m margin-left-l">
  <div class="link-container padding-top-s padding-bottom-xs">
    <a class="page-header__link link line-height-l" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;header&quot;,&quot;evt_ga_label&quot;:&quot;click_fuereigentuemer&quot;}" href="//www.immobilienscout24.de/eigentuemer.html">Für Eigentümer:innen</a>
  </div>
</div>

<div class="grid-item"></div>

<div class="grid-item grid-item-fixed-width padding-vertical-m header-desk-margin-right-xxl header-lap-margin-right-xl header-palm-margin-right-xl">
  <div class="padding-top-xs">
    <a class="button top-navigation__button top-navigation__anbieten-button align-middle" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;header&quot;,&quot;evt_ga_label&quot;:&quot;click_fuer0€inserieren&quot;}" href="//www.immobilienscout24.de/anbieten.html?cmp_id=051921&amp;cmp_name=ppa_insertion&amp;cmp_position=brand_homepage&amp;cmp_creative=header_button">
      <span class="palm-hide">Inserieren ab 0 €</span>
      <span class="desk-hide lap-hide">Inserieren</span>
    </a>
  </div>
</div>
<div class="grid-item grid-item-fixed-width header-lap-padding-right-l header-palm-padding-right-l">
        <div class="grid grid-flex grid-fill-rows sso-login topnavigation__sso-login sso-login--show-avatar page-header__content palm-user-tab padding-vertical-m">
          <span class="grid-item palm-hide lap-hide"></span>
<div class="grid-item grid-item-fixed-width padding-top-xs">
  <a class="grid grid-flex link-container vertical-center sso-login-link" title="Mein Bereich" aria-label="Mein Bereich" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;header&quot;,&quot;evt_ga_label&quot;:&quot;click_icon&quot;}" target="_self" href="https://www.immobilienscout24.de/geschlossenerbereich/start.html?source=headericon&amp;sso_return=https%3A%2F%2Fwww.immobilienscout24.de%2FSuche%2Fradius%2Fwohnung-mieten%3Fcenterofsearchaddress%3DGie%25C3%259Fen%2520Kreis%3B%3B%3B1276007006005%3B%3BGie%25C3%259Fen%3B%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383%3B8.67789%3B5.0%26enteredFrom%3Done_step_search&amp;appName=is24main"><noscript>
      <span class="grid-item page-header__link link topnavigation__basic-konto topnavigation__sso-login--logged-out padding-left-s padding-top-xs padding-bottom-xs palm-hide lap-hide">Anmelden</span>
    </noscript>
    <span class="grid-item grid-item-fixed-width topnavigation__sso-login--logged-out margin-vertical-auto height-l padding-top-xs padding-bottom-xs">
      <span class="icon palm-line-height-m lap-line-height-m desk-line-height-l font-size-l">
        <svg width="24" height="24" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path d="M682.656 469.344c26.624-34.912 42.656-79.168 42.656-127.136v-.896.032C725.312 223.52 629.792 128 511.968 128s-213.344 95.52-213.344 213.344c.448 48.544 17.248 93.056 45.152 128.448l-.352-.448H213.28v384h85.344V554.688H725.28v298.656l85.344-42.656V469.344zM512 213.344c70.688 0 128 57.312 128 128s-57.312 128-128 128-128-57.312-128-128 57.312-128 128-128z"></path></svg>
      </span>
		</span>
    <span class="grid-item grid-item-fixed-width topnavigation__sso-login__user-avatar topnavigation__sso-login__user-avatar-logged-in topnavigation__sso-login--logged-in margin-vertical-auto height-l topnavigation__hasAvatar desk-width-36 desk-height-36 lap-height-36 lap-width-36 palm-height-28 palm-width-28"></span>
    <span class="grid-item topnavigation__basic-konto topnavigation__sso-login--logged-out page-header__link link padding-left-s padding-top-xs padding-bottom-xs palm-hide lap-hide">Anmelden</span>
    <span class="grid-item topnavigation__basic-konto topnavigation__sso-login--logged-in padding-left-s palm-hide lap-hide">
			<span class="grid-item one-whole topnavigation__sso-login__header padding-top-xs font-size-12 line-height-17">angemeldet als</span>
        <span class="grid-item one-whole topnavigation__sso-login__user-name"></span>
			<span class="grid-item one-whole topnavigation__sso-login__footer page-header__login-link link grid-item one-whole padding-bottom-xs font-size-12 line-height-17">zu meinem Bereich</span>
		</span>
  </a></div>
</div>
      </div>
    <div class="page-header__hamburger-wrapper grid-item grid-item-fixed-width desk-order-one-up header-desk-padding-top-s header-desk-padding-right-l header-lap-padding-top-xs">
  <div class="page-header__hamburger-container header-desk-padding-top-xs header-palm-padding-top-xs" onclick="IS24.TEALIUM.tracking.report({evt_ga_category:&quot;navigation&quot;,evt_ga_action:&quot;hamburgermenu&quot;,evt_ga_label:&quot;open&quot;});">
    <div class="page-header__hamburger-button link-container desk-width-xl header-desk-padding-s" id="sidebarnavigation-slide-in-menuBtn">
      <span class="icon line-height-m font-size-l">
        <svg width="24" height="24" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path d="M810.656 298.656h-640v-85.344h682.656l-42.656 85.344zm-640 170.688h682.656v85.344H170.656zm0 256h682.656v85.344H170.656z"></path></svg>
      </span>
      <div class="page-header__hamburger-text palm-hide lap-hide line-height-m font-size-12">Menü</div>
    </div>
  </div>
</div>
</div>
  <div class="header__divider one-whole absolute-content desk-height-s"></div>

  <div id="sidebarnavigation-slide-in-menu" class="sidebarnavigation__slide-menu height-full hide">
  <nav class="sidebarnavigation" role="navigation">
    <!-- define chevron svg for reuse -->
    <svg style="display: none" xmlns="http://www.w3.org/2000/svg">
      <symbol id="chevron_down">
        <path d="M188.576 323.84L512 647.264 835.84 323.84 896 384 512 768 128 384l60.576-60.16z"></path>
      </symbol>
    </svg>
    <div class="grid grid-flex header-desk-padding-vertical-s header-lap-padding-l header-palm-padding-l">
      <div id="sidebarnavigation__closebtn" class="grid-item float-right desk-width-xxl header-desk-padding-vertical-s lap-one-whole palm-one-whole">
        <div class="float-right header-desk-padding-right-xs">
          <div id="sidebarnavigation__closebtn_action" class="sidebarnavigation__closebtn link-container desk-height-xxxl header-desk-padding-vertical-s header-lap-padding-top-xs header-desk-padding-right-s" onclick="IS24.TEALIUM.tracking.report({evt_ga_category:&quot;navigation&quot;,evt_ga_action:&quot;hamburgermenu&quot;,evt_ga_label:&quot;close&quot;});">
            <span class="icon palm-line-height-m lap-line-height-m font-size-l">
              <svg width="24" height="24" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path d="M896 188.16L835.424 128 512 451.424 188.16 128 128 188.16 451.424 512 128 835.424 188.16 896 512 572.576 835.424 896 896 835.424 572.576 512z"></path></svg>
            </span>
          </div>
        </div>
      </div>
      <div class="grid-item two-thirds header-desk-padding-vertical-m header-desk-padding-horizontal-l palm-hide lap-hide">
        <div class="sidebarnavigation__logo block padding-top-xs height-xl palm-hide lap-hide height-full">
          <img alt="ImmoScout24" src="//www.immobilienscout24.de/etc/designs/is24/img/immoscout24.svg">
        </div>
      </div>
    </div>
    <div class="grid grid-flex padding-top-xxl align-baseline">
      <div class="grid-item width-xxl grid-item-fixed-width"></div>
      <div id="sidebarnavigation-menu-container" class="grid-item lap-one-whole palm-one-whole padding-horizontal-l grid-item-fixed-width" data-cms-qa="is24-cms-page-nav_level1">
        <div comment="NavigationsBar" class="sidebarnavigation__headlines align-left">
          <div id="sidebarnavigation-secondary-links" class="sidebarnavigation-secondary-links desk-hide">
            <div class="sidebarnavigation-menu--secondary link-container margin-bottom-l" id="NavLayer6-Menu-Layer">
              <a class="link font-size-20 line-height-xl" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;header&quot;,&quot;evt_ga_label&quot;:&quot;click_fuersuchende&quot;}" href="//www.immobilienscout24.de/suchende.html">
                <span>Für Suchende</span>
              </a>
            </div>
            <div class="sidebarnavigation-menu--secondary link-container margin-bottom-l" id="NavLayer7-Menu-Layer">
              <a class="link font-size-20 line-height-xl" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;header&quot;,&quot;evt_ga_label&quot;:&quot;click_fuereigentuemer&quot;}" href="//www.immobilienscout24.de/eigentuemer.html">
                <span>Für Eigentümer:innen</span>
              </a>
            </div>
            <div class="sidebarnavigation__divider margin-bottom-l one-whole"></div>
          </div>
          <div class="sidebarnavigation-menu link-container margin-bottom-l" id="NavLayer1-Menu-Layer">
            <p class="link font-size-18 line-height-29 ">Suchen</p>
          </div>

          <div class="sidebarnavigation-menu link-container margin-bottom-l" id="NavLayer2-Menu-Layer">
            <p class="link font-size-18 line-height-29 ">Verkaufen</p>
          </div>

          <div class="sidebarnavigation-menu link-container margin-bottom-l" id="NavLayer3-Menu-Layer">
            <p class="link font-size-18 line-height-29 ">Vermieten</p>
          </div>

          <div class="sidebarnavigation-menu link-container margin-bottom-l" id="NavLayer4-Menu-Layer">
            <p class="link font-size-18 line-height-29 ">Finanzieren</p>
          </div>

          <div class="sidebarnavigation-menu link-container margin-bottom-l" id="NavLayer5-Menu-Layer">
            <p class="link font-size-18 line-height-29 ">Umziehen</p>
          </div>
        </div>
      </div>

      <div class="grid grid-flex grid-fill-rows height-full one-whole absolute-content hide" id="sidebarnavigation-slide-submenu">
        <div class="grid-item desk-width-xxl header-lap-padding-left-l header-palm-padding-left-l grid-item-fixed-width">
          <div id="sidebarnavigation__backbtn" class="sidebarnavigation_backbtn link-container align-right padding-top-xs">
            <span class="icon palm-line-height-m lap-line-height-m desk-line-height-l font-size-l header-desk-padding-right-s">
              <svg width="24" height="24" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path d="M938.656 469.344h-689.92L529.472 188.16 469.312 128l-384 384 384 384 60.16-60.16-280.736-281.184H896l42.656-85.344z"></path></svg>
            </span>
          </div>
        </div>
        <div class="grid-item">
          <div class="sidebarnavigation-submenu padding-horizontal-l" id="NavLayer1-Submenu-Layer">
            <p class="font-size-20 line-height-xl">Suchen</p>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer1-Submenu-Layer-item1">
              <p class="link font-size-14 line-height-22">Wohnen</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer1-Submenu-Layer-list1">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_wohnen_mietwohnungen&quot;}" href="//www.immobilienscout24.de/wohnen/mietwohnungen.html">Mietwohnungen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_wohnen_eigentumswohnungen&quot;}" href="//www.immobilienscout24.de/wohnen/eigentumswohnung.html">Eigentumswohnungen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_wohnen_haeuserkaufen&quot;}" href="//www.immobilienscout24.de/wohnen/haus-kaufen.html">Häuser kaufen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_wohnen_haeusermieten&quot;}" href="//www.immobilienscout24.de/wohnen/haus-mieten.html">Häuser mieten</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_wohnen_auslandsimmobilien&quot;}" href="//www.immobilienscout24.de/auslandsimmobilien/">Auslandsimmobilien</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_wohnen_wgzimmer&quot;}" href="//www.immobilienscout24.de/wohnen/wg-zimmer.html">WG-Zimmer</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_wohnen_schufaauskunftbestellen&quot;}" href="//bonitaetscheck.immobilienscout24.de/">SCHUFA-Auskunft bestellen</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer1-Submenu-Layer-item2">
              <p class="link font-size-14 line-height-22">Neubau</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer1-Submenu-Layer-list2">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_neubau_neubauprojekte&quot;}" href="//www.immobilienscout24.de/neubau/">Neubauprojekte</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_neubau_hausbauen&quot;}" href="//www.immobilienscout24.de/bauen/">Haus bauen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_neubau_hausbaukataloge&quot;}" href="//www.immobilienscout24.de/bauen/hauskatalog.html">Hausbau-Kataloge</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_neubau_hausbauratgeber&quot;}" href="//www.immobilienscout24.de/wissen/bauen.html">Hausbau Ratgeber</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_neubau_grundstueckkaufen&quot;}" href="//www.immobilienscout24.de/Suche/de/grundstueck-kaufen">Grundstück kaufen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_neubau_hausbaupreise&quot;}" href="//www.immobilienscout24.de/wissen/bauen/haus-bauen-preise.html">Hausbau Preise</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer1-Submenu-Layer-item3">
              <p class="link font-size-14 line-height-22">Gewerbe</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer1-Submenu-Layer-list3">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_gewerbe_gewerbeimmobiliensuchen&quot;}" href="//www.immobilienscout24.de/gewerbe.html">Gewerbeimmobilien suchen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_gewerbe_lagerproduktion&quot;}" href="//www.immobilienscout24.de/gewerbe/lagerhalle.html">Lager &amp; Produktion</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_gewerbe_gastronomieflaechen&quot;}" href="//www.immobilienscout24.de/gewerbe/gastronomie-immobilien.html">Gastronomieflächen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_gewerbe_lagerraeumeboxen&quot;}" href="//www.immobilienscout24.de/gewerbe/lagerboxen-und-selfstorage-mieten.html">Lagerräume &amp; -boxen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_gewerbe_bueropraxis&quot;}" href="//www.immobilienscout24.de/gewerbe/bueroimmobilien.html">Büro &amp; Praxis</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_gewerbe_einzelhandel&quot;}" href="//www.immobilienscout24.de/gewerbe/einzelhandelsimmobilien.html">Einzelhandel</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_gewerbe_bueroaufzeit&quot;}" href="//www.immobilienscout24.de/gewerbe/buero-auf-zeit.html">Büro auf Zeit</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer1-Submenu-Layer-item4">
              <p class="link font-size-14 line-height-22">Service &amp; Ratgeber</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer1-Submenu-Layer-list4">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_serviceratgeber_ratgeberimmobilienkauf&quot;}" href="//www.immobilienscout24.de/wissen/kaufen.html">Ratgeber Immobilienkauf</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_serviceratgeber_tippsfuermieter&quot;}" href="//www.immobilienscout24.de/wissen/mieten.html">Tipps für Mieter</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_serviceratgeber_vorlagendownloads&quot;}" href="//www.immobilienscout24.de/ratgeber/checklisten-vorlagen.html">Vorlagen &amp; Downloads</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_serviceratgeber_immobilienwertermitteln&quot;}" href="//www.immobilienscout24.de/immobilienbewertung/immobilienwertberechnen.html">Immobilienwert ermitteln</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_serviceratgeber_immobilienpreise&quot;}" href="//atlas.immobilienscout24.de/">Immobilienpreise</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_suchen_serviceratgeber_kontakthilfe&quot;}" href="//www.immobilienscout24.de/kontakt/s/">Kontakt &amp; Hilfe</a> </li>
              </ul>
            </div>
          </div>

          <div class="sidebarnavigation-submenu padding-horizontal-l" id="NavLayer2-Submenu-Layer">
            <p class="font-size-20 line-height-xl">Verkaufen</p>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer2-Submenu-Layer-item1">
              <p class="link font-size-14 line-height-22">Jetzt loslegen</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer2-Submenu-Layer-list1">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_jetztloslegen_immobiliebewerten&quot;}" href="//www.immobilienscout24.de/immobilienbewertung/">Immobilie bewerten</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_jetztloslegen_immobilieinserieren&quot;}" href="//www.immobilienscout24.de/anbieten/">Immobilie inserieren</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_jetztloslegen_maklerempfehlungerhalten&quot;}" href="//www.immobilienscout24.de/immobilienmakler/">Maklerempfehlung erhalten</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_jetztloslegen_maklerselbstfinden&quot;}" href="//www.immobilienscout24.de/anbieter/immobilienmakler">Makler selbst finden</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer2-Submenu-Layer-item2">
              <p class="link font-size-14 line-height-22">Für Eigentümer:innen</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer2-Submenu-Layer-list2">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuereigentuemer_preisatlas&quot;}" href="//atlas.immobilienscout24.de/">Preisatlas</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuereigentuemer_hausverkaufenleitfaden&quot;}" href="//www.immobilienscout24.de/wissen/verkaufen/haus-verkaufen.html">Haus verkaufen Leitfaden</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuereigentuemer_ratgeberzumimmobilienverkauf&quot;}" href="//www.immobilienscout24.de/wissen/verkaufen.html">Ratgeber zum Immobilienverkauf</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuereigentuemer_eigentuemerbereich&quot;}" href="//www.immobilienscout24.de/meinkonto/meine-immobilien/">Eigentümerbereich</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer2-Submenu-Layer-item3">
              <p class="link font-size-14 line-height-22">Für Immobilien-Profis</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer2-Submenu-Layer-list3">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuerimmobilienprofis_produktweltundtipps&quot;}" href="//www.immobilienscout24.de/anbieten/gewerbliche-anbieter.html">Produktwelt &amp; Tipps</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuerimmobilienprofis_derneueprovisionssplit&quot;}" href="//www.immobilienscout24.de/anbieten/gewerbliche-anbieter/tipps/aktuelle-themen/bestellerprinzip-bei-kauf.html">Der neue Provisionssplit</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuerimmobilienprofis_branchenbuch&quot;}" href="//www.immobilienscout24.de/anbieter/">Branchenbuch</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_verkaufen_fuerimmobilienprofis_kundinwerden&quot;}" href="//www.immobilienscout24.de/lp/kunde-werden.html">Kund:in werden</a> </li>
              </ul>
            </div>
          </div>

          <div class="sidebarnavigation-submenu padding-horizontal-l" id="NavLayer3-Submenu-Layer">
            <p class="font-size-20 line-height-xl">Vermieten</p>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer3-Submenu-Layer-item1">
              <p class="link font-size-14 line-height-22">Immobilie vermieten</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer3-Submenu-Layer-list1">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilievermieten_kostenlosinserieren&quot;}" href="//www.immobilienscout24.de/anbieten/">Kostenlos inserieren</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilievermieten_wohnungvermieten&quot;}" href="//www.immobilienscout24.de/wissen/vermieten/wohnung-vermieten.html">Wohnung vermieten</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilievermieten_nachmieterfinden&quot;}" href="//www.immobilienscout24.de/anbieten/private-anbieter/nachmieter-suchen.html">Nachmieter finden</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilievermieten_wgzimmervermieten&quot;}" href="//www.immobilienscout24.de/wissen/vermieten/wg-vermieten.html">WG-Zimmer vermieten</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilievermieten_gewerbeflaechenvermieten&quot;}" href="//www.immobilienscout24.de/anbieten/gewerbe-vermieten.html">Gewerbeflächen vermieten</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer3-Submenu-Layer-item2">
              <p class="link font-size-14 line-height-22">Immobilie verwalten</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer3-Submenu-Layer-list2">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilieverwalten_einfachdigitalverwalten&quot;}" href="//www.immobilienscout24.de/anbieten/private-anbieter/lp/vermietetde.html">Einfach digital verwalten</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilieverwalten_mietvertragentwerfen&quot;}" href="//www.immobilienscout24.de/umzug/ratgeber/mietrecht/muster-mietvertrag.html">Mietvertrag entwerfen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilieverwalten_wohnungsuebergabeprotokoll&quot;}" href="//www.immobilienscout24.de/wissen/mieten/wohnungsuebergabeprotokoll.html">Wohnungsübergabeprotokoll</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_immobilieverwalten_nebenkostenerstellen&quot;}" href="//www.immobilienscout24.de/wissen/vermieten/nebenkostenabrechnung.html">Nebenkosten erstellen</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer3-Submenu-Layer-item3">
              <p class="link font-size-14 line-height-22">Service &amp; Ratgeber</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer3-Submenu-Layer-list3">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_serviceratgeber_vermietenratgeber&quot;}" href="//www.immobilienscout24.de/wissen/vermieten.html">Vermieten Ratgeber</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_serviceratgeber_energieausweisbestellen&quot;}" href="//www.immobilienscout24.de/energieausweis/">Energieausweis bestellen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_serviceratgeber_grundsteuerberechnen&quot;}" href="//www.immobilienscout24.de/eigentuemer/grundsteuerrechner1.html">Grundsteuer berechnen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_serviceratgeber_mietpreisentwicklungverfolgen&quot;}" href="//atlas.immobilienscout24.de/">Mietpreisentwicklung verfolgen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_serviceratgeber_kontakthilfe&quot;}" href="//www.immobilienscout24.de/kontakt/s/">Kontakt &amp; Hilfe</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer3-Submenu-Layer-item4">
              <p class="link font-size-14 line-height-22">Für Immobilien-Profis</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer3-Submenu-Layer-list4">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_fuerimmobilienprofis_produktwelttipps&quot;}" href="//www.immobilienscout24.de/anbieten/gewerbliche-anbieter.html">Produktwelt &amp; Tipps</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_vermieten_fuerimmobilienprofis_kundinwerden&quot;}" href="//www.immobilienscout24.de/lp/kunde-werden.html">Kund:in werden</a> </li>
              </ul>
            </div>
          </div>

          <div class="sidebarnavigation-submenu padding-horizontal-l" id="NavLayer4-Submenu-Layer">
            <p class="font-size-20 line-height-xl">Finanzieren</p>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer4-Submenu-Layer-item1">
              <p class="link font-size-14 line-height-22">Immobilie finanzieren</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer4-Submenu-Layer-list1">
                <li class="link-container margin-top-m"><a title="Beratung buchen" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_immobiliefinanzieren_finanzierungsberatung&quot;}" href="//www.immobilienscout24.de/baufinanzierung/finanzierungsberatung/">Beratung buchen</a></li>
                <li class="link-container margin-top-m"><a title="Finanzrahmen prüfen" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_immobiliefinanzieren_finanzrahmenpruefen&quot;}" href="//www.immobilienscout24.de/baufinanzierung/finanzrahmen-pruefen/">Finanzrahmen prüfen</a></li>
                <li class="link-container margin-top-m"><a title="Angebote erhalten" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_immobiliefinanzieren_finanzierungsangebote&quot;}" href="//www.immobilienscout24.de/baufinanzierung/finanzierungsangebote/">Angebote erhalten</a></li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer4-Submenu-Layer-item3">
              <p class="link font-size-14 line-height-22">Service &amp; Ratgeber</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer4-Submenu-Layer-list3">
                <li class="link-container margin-top-m"><a title="Finanzierung - So funktioniert's" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_serviceratgeber_finanzieren&quot;}" href="//www.immobilienscout24.de/baufinanzierung/finanzieren/">Finanzierung - So funktioniert's</a></li>
                <li class="link-container margin-top-m"><a title="Unsere Finanzierungsrechner" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_serviceratgeber_rechner&quot;}" href="//www.immobilienscout24.de/baufinanzierung/rechner/">Unsere Finanzierungsrechner</a></li>
                <li class="link-container margin-top-m"><a title="Ratgeber zur Finanzierung" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_serviceratgeber_tippszurimmobilienfinanzierung&quot;}" href="//www.immobilienscout24.de/wissen/kaufen/immobilie-finanzieren/">Ratgeber zur Finanzierung</a></li>
                <li class="link-container margin-top-m"><a title="Kontakt &amp; Hilfe" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_serviceratgeber_kontakthilfe&quot;}" href="//www.immobilienscout24.de/kontakt/s/">Kontakt &amp; Hilfe</a></li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer4-Submenu-Layer-item4">
              <p class="link font-size-14 line-height-22">Für Berater:innen</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer4-Submenu-Layer-list4">
                <li class="link-container margin-top-m"><a title="Produktwelt" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_fuerberaterinnen_produktwelt&quot;}" href="//www.immobilienscout24.de/baufinanzierung/produkte/">Produktwelt</a></li>
                <li class="link-container margin-top-m"><a title="BauFiManager Login" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_fuerberaterinnen_baufimanagerlogin&quot;}" href="//www.immobilienscout24.de/baufimanager/app/baufimanager/">BauFiManager Login</a></li>
                <li class="link-container margin-top-m"><a title="Kund:in werden" class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_finanzieren_fuerberaterinnen_kundinwerden&quot;}" href="//www.immobilienscout24.de/lp/kunde-werden/">Kund:in werden</a></li>
              </ul>
            </div>
          </div>

          <div class="sidebarnavigation-submenu padding-horizontal-l" id="NavLayer5-Submenu-Layer">
            <p class="font-size-20 line-height-xl">Umziehen</p>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer5-Submenu-Layer-item1">
              <p class="link font-size-14 line-height-22">Dein Umzug</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer5-Submenu-Layer-list1">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_deinumzug_umzugplanen&quot;}" href="//www.immobilienscout24.de/umzug/">Umzug planen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_deinumzug_mietvertragkuendigen&quot;}" href="//www.immobilienscout24.de/umzug/ratgeber/vorlagen/musterbrief-kuendigung.html">Mietvertrag kündigen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_deinumzug_umzugsunternehmenvergleichen&quot;}" href="//www.immobilienscout24.de/umzug/umzugsunternehmen/vergleichen.html">Umzugsunternehmen vergleichen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_deinumzug_umzugcheckliste&quot;}" href="//www.immobilienscout24.de/umzug/ratgeber/planen/umzug-checkliste.html">Umzug Checkliste</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_deinumzug_umzugdeutschland&quot;}" href="//www.immobilienscout24.de/umzug/regional.html">Umzug Deutschland</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_deinumzug_halteverbotszonenbestellen&quot;}" href="//www.immobilienscout24.de/umzug/halteverbot.html">Halteverbotszonen bestellen</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer5-Submenu-Layer-item2">
              <p class="link font-size-14 line-height-22">Ratgeber</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer5-Submenu-Layer-list2">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_ratgeber_umzugorganisieren&quot;}" href="//www.immobilienscout24.de/wissen/mieten/umzug-planen.html">Umzug organisieren</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_ratgeber_umzugskostenberechnen&quot;}" href="//www.immobilienscout24.de/umzug/umzugskosten.html">Umzugskosten berechnen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_ratgeber_hartz4umzug&quot;}" href="//www.immobilienscout24.de/wissen/mieten/hartz4.html">Hartz 4 Umzug</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_ratgeber_vorlagendownloads&quot;}" href="//www.immobilienscout24.de/wissen/mieten/vorlagen.html">Vorlagen &amp; Downloads</a> </li>
              </ul>
            </div>
            <div class="grid grid-flex grid-justify-space-between sidebarnavigation-submenu-heading link-container margin-top-xl" id="NavLayer5-Submenu-Layer-item3">
              <p class="link font-size-14 line-height-22">Für Umzugsunternehmen</p>
              <p class="accordion line-height-s">
                <svg width="14" height="14" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><use href="#chevron_down"></use></svg>
              </p>
              <ul class="sidebarnavigation-submenu-links one-whole" id="NavLayer5-Submenu-Layer-list3">
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_fuerumzugsunternehmen_umzugsunternehmeneintragen&quot;}" href="//www.immobilienscout24.de/lp/kunde-werden.html">Umzugsunternehmen eintragen</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_fuerumzugsunternehmen_umzugsmanager&quot;}" href="//manager.relocation.immobilienscout24.de/start">Umzugsmanager</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_fuerumzugsunternehmen_anfragenmanager&quot;}" href="//www.immobilienscout24.de/umzug/anfragen-manager/">Anfragen-Manager</a> </li>
                <li class="link-container margin-top-m"><a class="link font-size-14 line-height-22" data-event="evtrack" data-tracking="{&quot;evt_ga_category&quot;:&quot;navigation&quot;,&quot;evt_ga_action&quot;:&quot;hamburgermenu&quot;,&quot;evt_ga_label&quot;:&quot;click_umziehen_fuerumzugsunternehmen_produktwelttipps&quot;}" href="//www.immobilienscout24.de/umzug/editionen.html">Produktwelt &amp; Tipps</a> </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</div>
<div id="sidebarnavigation-overlay" class="sidebarnavigation-overlay height-full one-whole hide"></div>
</header>
<script type="text/javascript">
  !function(i,g){"use strict";i.IS24=i.IS24||{},IS24.core=IS24.core||{},IS24.core.extensions=IS24.core.extensions||{},IS24.core.extensions.topnavigation=IS24.core.extensions.topnavigation||{},IS24.core.extensions.sidebarnavigation=IS24.core.extensions.sidebarnavigation||{},IS24.TEALIUM=IS24.TEALIUM||{},IS24.STATIC=IS24.STATIC||{},IS24.STATIC.helpers=IS24.STATIC.helpers||{},IS24.STATIC.helpers.loadScript=function(e,n){var t=g.createElement("script");t.type="text/javascript",t.src=e,n&&void 0!==n.async&&(t.async=n.async),n&&void 0!==n.defer&&(t.defer=n.defer),g.getElementsByTagName("head")[0].appendChild(t)},IS24.STATIC.helpers.getLocation=function(){return i.location};var s,o,l,a,d={},c={resolveURLString:function(e){var n=-1!==e.indexOf("?"),t=-1!==e.indexOf("#");return{hostAndPath:(n?e.split("?"):e.split("#"))[0],search:n?e.substring(e.indexOf("?")).split("#")[0]:"",hash:t?e.substring(e.indexOf("#")):""}},attachLinkParameters:function(e,n){var t,i,s,o,a,r,l,d,c=/[^\w\-\s.,+%@&="[\]]/g,u={},m={},g=[];if(e&&e.href&&"object"==typeof n){for(d in n)n.hasOwnProperty(d)&&(t=d.replace(c,""),i=n[d].replace(c,""),u[t]=i);for(o=(s=this.resolveURLString(e.href)).search?s.search.substring(1).split("&"):[],l=0;l<o.length;l++)m[(a=o[l].split("="))[0]]=a[1];for(d in u)u.hasOwnProperty(d)&&(m[d]=u[d]);for(d in m)m.hasOwnProperty(d)&&g.push(d+"="+m[d]);r="?"+g.join("&"),e.href=s.hostAndPath+r+s.hash}},hasNecessaryDOMAPIs:function(e){for(var n=!0,t=0;t<e.length;t++)if(!(e[t]in i||e[t]in g||e[t]in g.body)){n=!1;break}return n},findMatchingMapping:function(e){var n,t,i={".sandbox-immobilienscout24.de":{ssoDomain:"sso.sandbox-immobilienscout24.de",wwwDomain:"www.sandbox-immobilienscout24.de"},localhost:{ssoDomain:"sso.sandbox-immobilienscout24.de",wwwDomain:"www.sandbox-immobilienscout24.de"}};for(n in i)if(c.stringEndsWith(e,n)){t=i[n];break}return t},stringEndsWith:function(e,n){var t=e.indexOf(n);return-1!==t&&t===e.length-n.length},getPath:function(e){for(var n=[],t=e.target;t;)n.push(t),t=t.parentNode;return-1===n.indexOf(i)&&-1===n.indexOf(g)&&n.push(g),-1===n.indexOf(i)&&n.push(i),n}};function u(e){var n,t,i;a&&l&&(t=e.href,i=t,t=i="sso.immobilienscout24.de"!==a?t.replace("sso.immobilienscout24.de",a):i,n=i=i,t=n="www.immobilienscout24.de"!==l?i.replace("www.immobilienscout24.de",l):n,e.href=t)}function t(e){for(var n,t,i,s=g.querySelectorAll(".sso-login-link"),o=encodeURIComponent((t=e.ssoReturnUrl,i=t,i=l&&"www.immobilienscout24.de"!==l?t.replace(".immobilienscout24.de",".sandbox-immobilienscout24.de"):i)),a=encodeURIComponent(e.ssoAppName),r=0;r<s.length;r++)n=-1<s[r].href.indexOf("sso_return"),u(s[r]),s[r].classList.contains("sso-login-link--no-parameters")||(n&&!e.forceUpdateReturnUrl?c.attachLinkParameters(s[r],{appName:a}):c.attachLinkParameters(s[r],{sso_return:o,appName:a}))}function r(e){var n=g.querySelector(".sso-login"),t=g.querySelectorAll(".topnavigation__sso-login--logged-in"),i=g.querySelectorAll(".topnavigation__sso-login--logged-out"),s=g.querySelectorAll(".sso-login__user-name"),o=g.querySelectorAll(".topnavigation__sso-login__user-avatar"),a=g.querySelectorAll(".topnavigation__sso-login__user-name");e||console.error(new Error("jsonCallback, data is not set")),n||console.error(new Error("No Login Markup found")),n.classList.add("sso-login--logged-in"),n.classList.remove("padding-vertical-m");for(var r=0;r<t.length;r++)t[r].classList.remove("hide");for(var l=0;l<i.length;l++)i[l].classList.add("hide");var d="";void 0!==e.firstName&&(d=""+e.firstName),0===(d=void 0!==e.lastName?0<d.length?d+" "+e.lastName:""+e.lastName:d).length&&(d=e.userName);for(var c=0;c<s.length;c++)d&&s&&(s[c].innerHTML=d);if(e.imageUrl&&0!==o.length)for(var u=0;u<o.length;u++){var m=o[u].children[0]||g.createElement("img");m.src=e.imageUrl,m.alt=d,o[u].appendChild(m),o[u].classList.remove("hide")}0<d.length&&0!==a.length&&(n.classList.remove("padding-vertical-m"),a[0].innerHTML=d)}function m(){var e,n=g.querySelector(".sso-login"),t=g.querySelectorAll(".topnavigation__sso-login--logged-in"),i=g.querySelectorAll(".topnavigation__sso-login--logged-out");for(n.classList.remove("sso-login--logged-in"),n.classList.add("padding-vertical-m");e<t.length;e++)t[e].classList.add("hide");for(var s=0;s<i.length;s++)i[s].classList.remove("hide");localStorage.removeItem("headerData")}d.MenuBtn=function(){var e=g.getElementById("sidebarnavigation-slide-in-menuBtn"),n=g.getElementById("sidebarnavigation-slide-in-menu"),t=g.getElementById("sidebarnavigation-overlay");e.addEventListener("click",function(){d.menuBtn.openMenu()},!0),this.openMenu=function(){n.classList.remove("hide"),t.classList.remove("hide"),setTimeout(function(){n.classList.add("open"),t.classList.add("open")},50),g.body.style.overflow="hidden"}},d.Headlines=function(){var o,n=g.querySelectorAll(".sidebarnavigation-menu"),s=g.querySelectorAll(".sidebarnavigation-submenu-heading"),a=g.querySelectorAll(".sidebarnavigation-submenu-links"),r=g.querySelectorAll(".sidebarnavigation-submenu"),l=g.getElementById("sidebarnavigation-slide-submenu");this.init=function(){for(var e=0;e<n.length;e++)n[e].addEventListener("click",function(){d.headlines.menuController(this)},!0);for(e=0;e<s.length;e++)s[e].addEventListener("click",function(){d.headlines.submenuController(this)},!0)},this.menuController=function(e){for(var n=e.id.replace("Menu","Submenu"),t=(o=g.getElementById(n)).querySelectorAll(".sidebarnavigation-submenu-heading"),i=o.querySelectorAll(".sidebarnavigation-submenu-links"),s=0;s<t.length;s++)0===s?t[s].classList.add("active"):t[s].classList.remove("active");for(s=0;s<i.length;s++)0===s?i[s].classList.remove("hide"):i[s].classList.add("hide");for(s=0;s<r.length;s++)r[s].id!==n?r[s].classList.add("hide"):r[s].classList.remove("hide");l.classList.remove("hide"),setTimeout(function(){l.classList.add("open")},100)},this.submenuController=function(e){for(var n=e.id.replace("item","list"),t=g.getElementById(n),i=0;i<s.length;i++)s[i].id!==e.id&&s[i].classList.remove("active");setTimeout(function(){for(i=0;i<a.length;i++)a[i].classList.add("hide");t.classList.remove("hide"),setTimeout(function(){e.classList.add("active")},50)},550)}},d.SlideInMenu=function(){g.getElementById("sidebarnavigation-overlay").addEventListener("click",function(){d.closeBtn.closeMenu()},!0)},d.CloseBtn=function(){var e=g.getElementById("sidebarnavigation__closebtn"),n=g.getElementById("sidebarnavigation-slide-in-menu"),t=g.getElementById("sidebarnavigation-overlay"),i=g.getElementById("sidebarnavigation-slide-submenu");e.addEventListener("click",function(){d.closeBtn.closeMenu()},!0),g.onkeyup=function(e){27===e.keyCode&&d.closeBtn.closeMenu()},this.closeMenu=function(){n.classList.remove("open"),t.classList.remove("open"),setTimeout(function(){i.classList.remove("open"),i.classList.add("hide"),n.classList.add("hide"),t.classList.add("hide")},350),g.body.style.overflow=""}},d.BackBtn=function(){var e=g.getElementById("sidebarnavigation__backbtn"),n=g.getElementById("sidebarnavigation-slide-submenu");e.addEventListener("click",function(){d.backBtn.backBtnController(this)},!0),this.backBtnController=function(e){n.classList.remove("open"),setTimeout(function(){n.classList.add("hide")},350)}},IS24.STATIC.router=(s=g.querySelectorAll(".topnavigation__sso-login "),o=g.querySelectorAll(".link-container"),{markActiveLink:function(){var e=i.location.pathname.replace(".html","");if(void 0!==e&&0!==e.length&&"/"!==e){var n=0;if("/scoutmanager/dashboard/"===e||"/meinkonto/dashboard/"===e)for(n=0;n<s.length;n++)s[n].getElementsByClassName("link-container")[n].classList.add("active");else for(n=0;n<o.length;n++){var t=o[n].getElementsByClassName("page-header__link");t[0]&&t[0].href&&t[0].href.includes(e)&&o[n].classList.add("active")}}}}),IS24.STATIC.sso={updateLoginStatus:function(e){(n=localStorage.getItem("headerData"))&&r(JSON.parse(n));var n={ssoReturnUrl:IS24.ssoReturnUrl||IS24.STATIC.helpers.getLocation().href,ssoAppName:IS24.ssoAppName||"is24main",forceUpdateReturnUrl:e&&e.forceUpdateReturnUrl,requestUserData:!e||e.requestUserData},e=c.findMatchingMapping(IS24.STATIC.helpers.getLocation().hostname);l=e?e.wwwDomain:void 0,a=e?e.ssoDomain:void 0,t(n),n.requestUserData&&IS24.STATIC.sso.requestUserData()},requestUserData:function(){var e=new XMLHttpRequest,n=(e.withCredentials=!0,"https://"+((n=c.findMatchingMapping(IS24.STATIC.helpers.getLocation().hostname))?n.wwwDomain:"www.immobilienscout24.de")+"/meinkonto/api/v1/headerInfo");e.onreadystatechange=function(){var n;if(4===this.readyState&&200===this.status){try{n=JSON.parse(this.responseText)}catch(e){console.error(new Error("[UserHeaderAPI] Could not parse JSON return val... \n "+e.message)),n={},m()}void 0!==n.userName&&void 0!==n.imageUrl?(localStorage.setItem("headerData",JSON.stringify(n)),r(n)):m()}else 4===this.readyState&&200!==this.status&&(console.error(new Error("[header] API Request failed.")),m())},e.open("GET",n,!0),e.send()}},IS24.core.extensions.sidebarnavigation.init=function(){d.closeBtn=new d.CloseBtn,d.backBtn=new d.BackBtn,d.menuBtn=new d.MenuBtn,d.headlines=new d.Headlines,d.slideInMenu=new d.SlideInMenu,d.headlines.init(),d.breakpoint_palm=668}}(window,document);</script>

<script type="text/javascript">

    // initialize login status before DOM ready to avoid flickering
    if (window.IS24 && IS24.STATIC && IS24.STATIC.sso && IS24.STATIC.sso.updateLoginStatus) {
      IS24.STATIC.sso.updateLoginStatus();
    }

    (function () {
      function initializeHeader() {
        if (window.IS24 && IS24.STATIC && IS24.STATIC.router && IS24.STATIC.router.markActiveLink) {
          IS24.STATIC.router.markActiveLink();
        }
        if (window.IS24 && IS24.core && IS24.core.extensions && IS24.core.extensions.sidebarnavigation) {
          IS24.core.extensions.sidebarnavigation.init();
        }
      }

      if (
        document.readyState === "complete" ||
        (document.readyState !== "loading" && !document.documentElement.doScroll)
      ) {
        // execute immediately if DOMContentLoaded has already fired
        // this is a fallback for applications which load the header asynchronously and need to execute this script after DOM Ready
        initializeHeader();
      } else {
        if ("addEventListener" in document) {
          document.addEventListener("DOMContentLoaded", function () {
            initializeHeader();
          });
        } else if ("attachEvent" in document) {
          document.attachEvent("onreadystatechange", function () {
            if (document.readyState === "complete") {
              initializeHeader();
            }
          });
        }
      }
    }());
  </script>





      </div>
    </div>
  

  
    
      <div id="resultlistpage"><div id="is24-page-loaded"><div class="content-wrapper content-wrapper--palm-stretch content-wrapper--lap-stretch"><s24-ad-slot class="" ad-unit-path="/4467/IS24_DE/resultlist/out_of_page" id="out_of_page" data-viewmode="" aria-hidden="true" preload="0" out-of-page="true" size-map-320x300="1x1" size-map-0x0=""></s24-ad-slot><div id="billboard" class="banner-top-placeholder"><div class="banner-top-placeholder  ad-placeholder"><s24-ad-slot class="ad-banner align-center " ad-unit-path="/4467/IS24_DE/resultlist/banner_top" id="banner_top" data-viewmode="LIST" aria-hidden="true" preload="200" size-map-0x0="" size-map-669x0="320x50,320x100,680x220" size-map-728x0="680x220" size-map-800x0="680x220,800x250" size-map-970x0="680x220,800x250,970x250"></s24-ad-slot></div></div></div><div class="sticky-filter" data-sticky-header="true"><div id="observer-interceptor" data-observer-intercept=""></div><div class="content-wrapper content-wrapper--palm-stretch negate-lap-stretch search-header-outer palm-hide" data-sticky-header="true"><div id="searchHead" class="search-header"><div class="grid grid-flex palm-hide margin-bottom-l"><h1 class="palm-hide resultListHeadline font-ellipsis font-l font-light font-line-s margin-bottom-none" data-is24-qa="resultlist-headline"><span class="font-normal no-of-results-highlighter margin-right-xs" data-is24-qa="resultlist-resultCount">21<!-- -->&nbsp;</span><span>Mietwohnungen im Umkreis von 5 km von Gießen (Kreis)</span></h1><button id="saveSearchHeaderLink" class="link-text margin-left-s save-search-link saveSearchHeaderLinkSave"><span class="s24-icons-s24_heart_magnifier_24 margin-right-xs"></span><span>Suche speichern</span></button></div><div class="header-controls"><div id="header-controls"><div class="grid grid-flex grid-fill-rows grid-align-center gutter-horizontal-l gutter-vertical-l negate-palm-stretch"><div data-testid="cockpit-desk" class="grid-item grid-item-fixed-width lap-one-whole desk-one-whole"><div id="reactCockpit" class="react-cockpit cockpit"><div class="grid grid-flex grid-fill-rows gutter-m"><div class="grid-item grid-item-fixed-width hide"><div class=""><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><button class="button button-secondary button-icon-standalone-small" aria-label="KI fake door"><span class="inline-block ai-fake-door-button-icon"></span></button></span></div></div><div class="grid-item one-half"><div class="react-cockpit__outside-criteria"><div class="grid grid-flex grid-fill-rows gutter-m"><div class="grid-item" style="width:34%"><div class="criterion"><div class="drop-down-layer-container"><div class="cockpit__region-selection-button" data-is24-qa="regionSelection"><div class="grid grid-flex grid-fill-rows"><div class="grid-item one-half" title="Gießen (Kreis)-Gießen"><div class="select-container fake-dropdown"><span class="input-icon-left"><svg width="20" height="20" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><circle stroke-width="2" stroke="currentColor" cx="10" cy="10" r="8"></circle><circle fill="currentColor" cx="10" cy="10" r="3"></circle></g></svg></span><div class="select cockpit__region-selection-button-location-label">Gießen (Kreis)-Gießen</div></div></div></div></div></div></div></div><div class="grid-item" style="width:22%"><div class="criterion"><div class="drop-down-layer-container"><div class="select-container fake-dropdown"><div data-is24-qa="priceRangeWithType" class="select">bis 800 €</div></div></div></div></div><div class="grid-item" style="width:22%"><div class="criterion"><div class="drop-down-layer-container"><div class="select-container fake-dropdown"><div data-is24-qa="netAreaRange" class="select">Wohnfläche</div></div></div></div></div><div class="grid-item" style="width:22%"><div class="criterion"><div class="drop-down-layer-container"><div class="select-container fake-dropdown"><div data-is24-qa="numberOfRoomsRange" class="select">ab 2 Zi.</div></div></div></div></div></div></div></div><div class="grid-item grid-item-fixed-width"><div><button type="button" class="button searchFilterButtonQA adapt-search button-secondary" data-testid="searchFilterButton"><span>Weitere Filter</span></button></div></div></div></div></div></div></div></div></div></div></div><div id="result-list-content" class="result-list-content"><div role="main" class="content-wrapper content-wrapper--palm-stretch"><div class="grid grid-flex grid-fill-rows grid-align-center negate-palm-stretch palm-hide padding-top-xl padding-bottom-xl"><div id="mapToggle" class="grid-item grid-item-fixed-width absolute-reference"><div data-testid="mapToggleButtons" class="map-toggle"><button data-testid="mapToggleListMode" class="button-primary map-toggle font-s padding-vertical-s padding-horizontal-l"><span class="s24-icons-s24_menu_burger_24"></span><span class="palm-hide">&nbsp;<!-- -->Liste</span></button><button data-testid="mapToggleMapMode" class="button map-toggle font-s padding-vertical-s padding-horizontal-l"><span class="s24-icons-s24_map_24"></span><span class="palm-hide">&nbsp;<!-- -->Karte</span></button><button type="button" data-testid="mapTogglePriceInsightsMode" class="button map-toggle font-s padding-vertical-s padding-horizontal-l"><span class="s24-icons-s24_map_euro_24"></span><span class="palm-hide">&nbsp;<!-- -->Preisatlas</span></button></div></div><div class="grid-item automatic-width margin-none padding-none"></div><div id="sorting-control" class="grid-item grid-item-fixed-width align-right"><div class="cockpit__sorting-control sortForm margin-none"><div class="fake-dropdown lap-hide desk-hide"><select class="select" name="sortingControl"><option selected="" value="0">Standardsortierung</option><option value="3">Kaltmiete (höchste zuerst)</option><option value="4">Kaltmiete (niedrigste zuerst)</option><option value="1">Entfernung (niedrigste zuerst)</option><option value="5">Zimmeranzahl (höchste zuerst)</option><option value="6">Zimmeranzahl (niedrigste zuerst)</option><option value="7">Wohnfläche (größte zuerst)</option><option value="8">Wohnfläche (kleinste zuerst)</option><option value="2">Aktualität (neueste zuerst)</option></select><div class="icon-dropdown background-white"><span class="s24-icons-s24_arrows_up_down_24 font-xl"></span></div></div><div><div class="cockpit__sorting-info palm-hide lap-hide"><span id="sortingControlLabel">Sortieren nach:</span><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><i class="s24-icons-s24_info_circle_24 cockpit__sorting-icon-info" role="button"></i></span></div><div class="sorting-html-control inline-block palm-hide"><button class="link-text sorting-label label"><span class="margin-right-xs"><span class="s24-icons-s24_arrows_up_down_24 font-m align-bottom inline-block sort-image"></span></span><span class="name margin-right-xs">Standardsortierung</span></button><div class="drop-down-layer sorting-dropdown border background-white align-left hide"><div class="selected entry">Standardsortierung</div><div class="entry">Kaltmiete (höchste zuerst)</div><div class="entry">Kaltmiete (niedrigste zuerst)</div><div class="entry">Entfernung (niedrigste zuerst)</div><div class="entry">Zimmeranzahl (höchste zuerst)</div><div class="entry">Zimmeranzahl (niedrigste zuerst)</div><div class="entry">Wohnfläche (größte zuerst)</div><div class="entry">Wohnfläche (kleinste zuerst)</div><div class="entry">Aktualität (neueste zuerst)</div></div></div></div></div></div></div><div id="searchMapContainer" class="listings-content-area grid margin-bottom-m"><div id="listContainer" class="listings-content-area__listings grid-item palm-one-whole lap-one-whole"><div id="listings"><ul id="resultListItems" class="result-list" data-testid="result-list-items"><li class="result-list__listing " data-id="147698275"><article data-item="result" data-obid="147698275" id="result-l-147698275" class="result-list-entry result-list-entry--l paywall-listing" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="palm-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 4693px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-5" width="420" height="315" class="gallery__image block height-full" src="https://pictures.immobilienscout24.de/listings/e0c9bc49-a05a-4e1d-bb89-23aa43155513-1684709476.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-0" width="420" height="315" class="gallery__image block height-full" src="https://pictures.immobilienscout24.de/listings/9065500a-0387-4cd3-acd6-caa9d7ee7ebc-1684709471.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ed6a4736-7849-4ca8-8022-e53528a3e0d0-1684709472.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f0034c75-6c0f-40fb-812c-a01756fb508d-1684709473.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/34c091b0-842b-4943-b57e-5307238f98b9-1684709474.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bcdb6ea5-b984-40d2-9db0-195533a79750-1684709475.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/e0c9bc49-a05a-4e1d-bb89-23aa43155513-1684709476.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-0" width="420" height="315" class="gallery__image block height-full" src="https://pictures.immobilienscout24.de/listings/9065500a-0387-4cd3-acd6-caa9d7ee7ebc-1684709471.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ed6a4736-7849-4ca8-8022-e53528a3e0d0-1684709472.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f0034c75-6c0f-40fb-812c-a01756fb508d-1684709473.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/34c091b0-842b-4943-b57e-5307238f98b9-1684709474.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bcdb6ea5-b984-40d2-9db0-195533a79750-1684709475.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-0-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/e0c9bc49-a05a-4e1d-bb89-23aa43155513-1684709476.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">6</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="desk-hide lap-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Freundliche 3-Zimmer-Wohnung mit Einbauküche in Gießen</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147698275" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Innenstadt, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147698275" data-go-to-expose-id="147698275"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">500 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">70 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Keller</li><li class="margin-top-none margin-bottom-xs">WG-geeignet</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147698275" data-go-to-expose-id="147698275" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div><div class="grid-item one-third font-ellipsis"></div><div class="grid-item grid-item-fixed-width"></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147627798"><article data-item="result" data-obid="147627798" id="result-l-147627798" class="result-list-entry result-list-entry--l false" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 7581px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/5bfaf1bf-2d75-4508-b40e-93f7dd289e0b-1682406866.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/e895c8cc-2d12-4d7f-9330-b3a249dab35e-1682406830.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a35025ff-6399-4f56-8d02-6051e8f45973-1682406837.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/cb7c608a-44ab-4460-93f7-114488d833fa-1682406840.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f1a5f200-f89c-4ad9-a1c0-96af01a8c052-1682406841.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/aaee8252-d0de-4601-b062-ca6ed882f40b-1682406842.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4cee33c4-be32-467c-af69-61af4f6719b3-1682406843.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/0269824f-202b-44d3-aa6c-e8306240181e-1682406844.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/274d8fed-9920-496f-acc1-2d7fec7fedbe-1682406863.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a57c65eb-8b83-4a58-be8e-85f4cf874e63-1682406864.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/5bfaf1bf-2d75-4508-b40e-93f7dd289e0b-1682406866.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/e895c8cc-2d12-4d7f-9330-b3a249dab35e-1682406830.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a35025ff-6399-4f56-8d02-6051e8f45973-1682406837.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/cb7c608a-44ab-4460-93f7-114488d833fa-1682406840.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f1a5f200-f89c-4ad9-a1c0-96af01a8c052-1682406841.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/aaee8252-d0de-4601-b062-ca6ed882f40b-1682406842.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4cee33c4-be32-467c-af69-61af4f6719b3-1682406843.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/0269824f-202b-44d3-aa6c-e8306240181e-1682406844.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/274d8fed-9920-496f-acc1-2d7fec7fedbe-1682406863.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="18" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a57c65eb-8b83-4a58-be8e-85f4cf874e63-1682406864.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="19" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-1-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/5bfaf1bf-2d75-4508-b40e-93f7dd289e0b-1682406866.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">10</span></div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths">In Gießens schönstem Viertel an der Wieseck: Offene 2 Zimmer-Maisonette-Wohnung mit Balkon, Löber...</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">0.39 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147627798" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Löberstr. 17a, Innenstadt, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147627798" data-go-to-expose-id="147627798"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">680 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">68 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Keller</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147627798" data-go-to-expose-id="147627798" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/147627798" data-go-to-expose-id="147627798" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Claus R. Menges GmbH</span><span class="font-ellipsis">Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.17215" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147677400"><article data-item="result" data-obid="147677400" id="result-l-147677400" class="result-list-entry result-list-entry--l paywall-listing" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="palm-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 10469px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/606ef35e-c110-4e1b-b1ee-e6ff3035309e-1684060797.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4c7ae478-5168-4a8e-ac6a-e525ef77766b-1684060867.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d708dd3d-dbdc-4987-b4e6-1bac63f6a822-1684060862.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/94e1e4d5-5997-4600-9d55-c20c35565f99-1684060853.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/95302e36-9181-47b2-82f8-87f922f418b9-1684060843.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ccb90651-c22f-481e-bb60-4007314c3cec-1684060799.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/60520a90-91fb-4f53-acc5-86169b7dd55d-1684060803.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2ccca4b3-cc73-43aa-a79f-0c8934dc9801-1684060870.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bc2af19a-0f1f-4621-a2fa-704b37282a02-1684060808.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c3157e6f-3338-4c61-90eb-086f5d70d233-1684060819.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9f1228a1-5bcd-43e8-9535-c6ff24c441c0-1684060827.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/cfbd85ed-dab9-43d1-bcbb-fdb11551e0a6-1684060835.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-11" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f0c8ffb0-942f-4121-99ac-6769fe88da00-1684071212.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-12" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/766ab9d9-a40b-4d1d-a61a-ccb91777f91d-1684060874.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/606ef35e-c110-4e1b-b1ee-e6ff3035309e-1684060797.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4c7ae478-5168-4a8e-ac6a-e525ef77766b-1684060867.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d708dd3d-dbdc-4987-b4e6-1bac63f6a822-1684060862.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/94e1e4d5-5997-4600-9d55-c20c35565f99-1684060853.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/95302e36-9181-47b2-82f8-87f922f418b9-1684060843.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="18" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ccb90651-c22f-481e-bb60-4007314c3cec-1684060799.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="19" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/60520a90-91fb-4f53-acc5-86169b7dd55d-1684060803.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="20" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2ccca4b3-cc73-43aa-a79f-0c8934dc9801-1684060870.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="21" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bc2af19a-0f1f-4621-a2fa-704b37282a02-1684060808.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="22" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c3157e6f-3338-4c61-90eb-086f5d70d233-1684060819.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="23" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9f1228a1-5bcd-43e8-9535-c6ff24c441c0-1684060827.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="24" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/cfbd85ed-dab9-43d1-bcbb-fdb11551e0a6-1684060835.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="25" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-11" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f0c8ffb0-942f-4121-99ac-6769fe88da00-1684071212.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="26" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-12" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/766ab9d9-a40b-4d1d-a61a-ccb91777f91d-1684060874.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="27" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-2-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/606ef35e-c110-4e1b-b1ee-e6ff3035309e-1684060797.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">14</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="desk-hide lap-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Walltorstraße 34, 35390 Gießen</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">0.61 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147677400" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Walltorstraße 34, Innenstadt, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147677400" data-go-to-expose-id="147677400"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">725 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">80 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Keller</li><li class="margin-top-none margin-bottom-xs">Gäste-WC</li><li class="margin-top-none margin-bottom-xs">Aufzug</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147677400" data-go-to-expose-id="147677400" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div><div class="grid-item one-third font-ellipsis"></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.19238817" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="align-center banner_developer_realtors_5th_position ad-placeholder"><s24-ad-slot class="is24-adplace align-center" ad-unit-path="/4467/IS24_DE/resultlist/banner_developer_realtors_5th_position" id="banner_developer_realtors_5th_position" data-viewmode="LIST" aria-hidden="true" preload="0" immediate="true" ad-label-center="true" ad-label-text="Anzeige" ad-label-top="true" size-map-0x0="320x100,fluid" size-map-468x0="320x100,fluid" size-map-728x0="680x220,fluid" size-map-776x0="680x220,fluid" size-map-848x0="800x250,680x220,fluid" size-map-997x0="680x220,fluid" size-map-1048x0="680x220,fluid" size-map-1120x0="800x250,680x220,fluid"></s24-ad-slot></li><li class="result-list__listing " data-id="139035681"><article data-item="result" data-obid="139035681" id="result-l-139035681" class="result-list-entry result-list-entry--l false" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 6859px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/719e5a06-34cd-4132-8df6-1d3f74f30f98-1588840488.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2021945b-9383-4521-af2f-43eb08c38078-1588840466.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/17ceb351-3058-40d9-b864-dc51d6d3c4c5-1588840468.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d20fd1fa-95c9-4155-9d21-7052a4d85c1a-1588840471.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/83046709-c52a-4360-a415-62f415ddee37-1588840474.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c0e787d5-6516-4379-bc53-c44b39278dc7-1588840476.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/71e27771-ce59-40c2-8803-ec1c52c80fea-1588840478.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/5172d3a4-5c17-40b5-bdfd-e8d3fdb6930b-1588840480.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fd21df28-9e47-46b3-98d3-45af0a6e533b-1588840484.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/719e5a06-34cd-4132-8df6-1d3f74f30f98-1588840488.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2021945b-9383-4521-af2f-43eb08c38078-1588840466.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/17ceb351-3058-40d9-b864-dc51d6d3c4c5-1588840468.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d20fd1fa-95c9-4155-9d21-7052a4d85c1a-1588840471.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/83046709-c52a-4360-a415-62f415ddee37-1588840474.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c0e787d5-6516-4379-bc53-c44b39278dc7-1588840476.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/71e27771-ce59-40c2-8803-ec1c52c80fea-1588840478.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/5172d3a4-5c17-40b5-bdfd-e8d3fdb6930b-1588840480.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fd21df28-9e47-46b3-98d3-45af0a6e533b-1588840484.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-3-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/719e5a06-34cd-4132-8df6-1d3f74f30f98-1588840488.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">9</span></div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths">Nur für Gießener Senior:innen mit WBS: Großzügige 2 Zimmer-Wohnung mit Balkon - Sorglos leben in ...</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">0.95 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="139035681" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Curtmannstr. 38, Gießen-Ost, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/139035681" data-go-to-expose-id="139035681"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">335 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">64 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Keller</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/139035681" data-go-to-expose-id="139035681" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/139035681" data-go-to-expose-id="139035681" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Claus R. Menges GmbH</span><span class="font-ellipsis">Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.17215" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147564321"><article data-item="result" data-obid="147564321" id="result-l-147564321" class="result-list-entry result-list-entry--l false" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 3249px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/7c6b2a34-10b5-4f91-8dd0-196f2b358679-1680196827.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/8f7263a2-95ca-407c-85dd-4e34cc947952-1680196820.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f15c7270-1ee5-48ca-b950-ff0ddda1cc52-1680196823.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/dfa37c2b-b8fc-4952-9dab-9d22a27495a3-1680196826.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/7c6b2a34-10b5-4f91-8dd0-196f2b358679-1680196827.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/8f7263a2-95ca-407c-85dd-4e34cc947952-1680196820.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f15c7270-1ee5-48ca-b950-ff0ddda1cc52-1680196823.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/dfa37c2b-b8fc-4952-9dab-9d22a27495a3-1680196826.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-4-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/7c6b2a34-10b5-4f91-8dd0-196f2b358679-1680196827.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">4</span></div><div class="result-list-entry__eco-flag"><svg width="36" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><path fill="#4F9D2A" d="M0 0h28l8 8.253L28 16H0z"></path><text font-size="14" font-weight="500" fill="#FFF"><tspan x="4" y="13">A</tspan></text></g></svg></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="result-list-entry__eco-flag"><svg width="36" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><path fill="#4F9D2A" d="M0 0h28l8 8.253L28 16H0z"></path><text font-size="14" font-weight="500" fill="#FFF"><tspan x="4" y="13">A</tspan></text></g></svg></div><div class="small-listings--realtor-logo-container"><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Mit gleich 2 Balkonen! Lichtdurchflutete, moderne und attraktive 2 Zimmer-Wohnung Nähe Bahnhof+In...</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">1.06 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147564321" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Schuppstr. 1, Gießen-Süd, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147564321" data-go-to-expose-id="147564321"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">730 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">54 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Keller</li><li class="margin-top-none margin-bottom-xs">...</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147564321" data-go-to-expose-id="147564321" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/147564321" data-go-to-expose-id="147564321" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Claus R. Menges GmbH</span><span class="font-ellipsis">Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.17215" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><nav class="desk-hide background-white"><section class="teaser-section"><div class="grid grid-flex grid-justify-center teaser-flex-container"><div class="Indicator_indicator__IhewW Indicator_indicator--brand__4p0ak brand-name margin-bottom-s"><span>Kostenlos vergleichen</span></div><h5 class="align-center margin-bottom-m" data-testid="relocation-teaser-headline">Spare bis zu 42 % beim Umzug</h5><p class="input-hint align-center margin-bottom-s">PLZ deines Wohnorts:</p><div class="teaser-input input-text-container margin-bottom-s palm-margin-bottom-m"><input type="text" data-testid="postal-code-input" class="input-text" placeholder="z. B. 14057"></div><a data-testid="redirection-link" href="/umzug/umzugsunternehmen/vergleichen.html?cmp_id=10-052160&amp;cmp_name=relocation_leadengine&amp;cmp_position=search_resultlist_rent&amp;cmp_creative=mobile_inlist_teaser"><button class="teaser-button margin-bottom-m Button_button__DdOl8" qa-regression-tag="button">Jetzt Preise vergleichen</button></a></div></section></nav><li class="result-list__listing " data-id="138407506"><article data-item="result" data-obid="138407506" id="result-l-138407506" class="result-list-entry result-list-entry--l false" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 10469px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/60d5531f-adae-4a74-98af-e68b73fb57f8-1582183616.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/0f3348ac-c493-48a2-8a07-cce22c67e9e3-1582183031.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/8eb48d11-f659-427d-bf5b-c9a753e532d5-1582183226.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/87882819-ac44-4615-ae48-7481905922ac-1621582961.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ec925094-23f8-41f1-be8b-83739bbea1ff-1582183308.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a6a4517c-2350-48ed-88e1-5ce8166f28a5-1621582967.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9bcfad74-68ef-4085-b2af-0e6f483ced6a-1582183579.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9d9144ec-103e-48f5-8a4a-f692d0e4e64d-1621582971.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d78c663a-c47d-4a96-805d-6db0fbbd6754-1582183434.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f8b9afea-b4c4-4b53-b2f4-80a26f749bbe-1582183371.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d7c5e8ed-0520-45d5-a79c-132210b905a7-1621582978.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/eb5043bc-6c62-4007-87b6-4beef89fbf35-1582183484.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-11" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/92796381-7f6d-42f5-a7e3-2716b7c3f97e-1621582985.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-12" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/8d74427e-199d-44d1-92bc-6428bbaf5bfe-1582183514.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/60d5531f-adae-4a74-98af-e68b73fb57f8-1582183616.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/0f3348ac-c493-48a2-8a07-cce22c67e9e3-1582183031.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/8eb48d11-f659-427d-bf5b-c9a753e532d5-1582183226.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/87882819-ac44-4615-ae48-7481905922ac-1621582961.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ec925094-23f8-41f1-be8b-83739bbea1ff-1582183308.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="18" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a6a4517c-2350-48ed-88e1-5ce8166f28a5-1621582967.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="19" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9bcfad74-68ef-4085-b2af-0e6f483ced6a-1582183579.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="20" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9d9144ec-103e-48f5-8a4a-f692d0e4e64d-1621582971.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="21" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d78c663a-c47d-4a96-805d-6db0fbbd6754-1582183434.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="22" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f8b9afea-b4c4-4b53-b2f4-80a26f749bbe-1582183371.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="23" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d7c5e8ed-0520-45d5-a79c-132210b905a7-1621582978.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="24" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/eb5043bc-6c62-4007-87b6-4beef89fbf35-1582183484.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="25" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-11" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/92796381-7f6d-42f5-a7e3-2716b7c3f97e-1621582985.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="26" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-12" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/8d74427e-199d-44d1-92bc-6428bbaf5bfe-1582183514.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="27" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-5-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/60d5531f-adae-4a74-98af-e68b73fb57f8-1582183616.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">14</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/b9800be2-5c4a-429c-9aa8-c41f65e2db52.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Bezahlbare 3-Zi-Wohnung mit Balkon</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">1.57 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="138407506" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Marburger Str. 86, Gießen-Nord, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/138407506" data-go-to-expose-id="138407506"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">750 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">78 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Gäste-WC</li><li class="margin-top-none margin-bottom-xs">Aufzug</li><li class="margin-top-none margin-bottom-xs">...</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/138407506" data-go-to-expose-id="138407506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/b9800be2-5c4a-429c-9aa8-c41f65e2db52.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/138407506" data-go-to-expose-id="138407506" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Ihr Vermietungsteam der Sucasa </span><span class="font-ellipsis">sucasa e.K.</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.12607949" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147463951"><article data-item="result" data-obid="147463951" id="result-l-147463951" class="result-list-entry result-list-entry--l false" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 8303px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/126b7795-aef2-4811-a0a1-0e519b804c58-1678160380.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ca4e064f-a24e-4fe7-a1a5-e472c6bc3290-1678169429.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c7f97afa-de7a-497f-b2cb-c962305bca68-1678349230.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d22933f1-3108-43ec-a1a4-b074d4b0daf9-1678160456.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/72d95a81-c521-4566-b466-886969cdc5d0-1678160403.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/576219ee-0099-4748-903e-13822a490902-1678160513.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/6509553b-e7eb-49c0-9cbe-295b4dc81c56-1678160555.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b8a1caaa-fd9e-4e3f-ac2d-fd8746c66c16-1678160675.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/71263bf2-4e01-4cdf-acb6-dd45b57d5059-1678160739.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/aaa8246d-0aae-42c3-86ec-67f784a56c36-1678160894.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bf85c057-a3bf-4521-b634-4ba8ea1c1b1b-1678160289.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/126b7795-aef2-4811-a0a1-0e519b804c58-1678160380.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ca4e064f-a24e-4fe7-a1a5-e472c6bc3290-1678169429.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c7f97afa-de7a-497f-b2cb-c962305bca68-1678349230.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d22933f1-3108-43ec-a1a4-b074d4b0daf9-1678160456.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/72d95a81-c521-4566-b466-886969cdc5d0-1678160403.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/576219ee-0099-4748-903e-13822a490902-1678160513.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/6509553b-e7eb-49c0-9cbe-295b4dc81c56-1678160555.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b8a1caaa-fd9e-4e3f-ac2d-fd8746c66c16-1678160675.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="18" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/71263bf2-4e01-4cdf-acb6-dd45b57d5059-1678160739.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="19" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/aaa8246d-0aae-42c3-86ec-67f784a56c36-1678160894.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="20" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bf85c057-a3bf-4521-b634-4ba8ea1c1b1b-1678160289.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="21" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-6-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/126b7795-aef2-4811-a0a1-0e519b804c58-1678160380.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">11</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/0657fe8d-22fc-4107-ad58-e8483ed68f16.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>frisch sanierte Wohnung am Stadtrand</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">2.04 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147463951" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Eichendorffring 137, Gießen-Ost, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147463951" data-go-to-expose-id="147463951"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">670 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">75 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Keller</li><li class="margin-top-none margin-bottom-xs">Aufzug</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147463951" data-go-to-expose-id="147463951" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/0657fe8d-22fc-4107-ad58-e8483ed68f16.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/147463951" data-go-to-expose-id="147463951" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Herr Marcus  Gehrhardt</span><span class="font-ellipsis">Erich Ries Immobilien- und Verwaltungs GmbH</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.403897" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="129475294"><article data-item="result" data-obid="129475294" id="result-l-129475294" class="result-list-entry result-list-entry--l false" data-listing-size="L" aria-label="listing-L"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 12635px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="is24-ex-video"><img alt="Videobild" class="block horizontal-center" id="listing-7-slide-16" data-video-id="iTlk3U9nLHF-5bn78WcjoQ" style="max-height:100%;max-width:100%;margin:auto;position:absolute;top:0;bottom:0;left:0;right:0" src="https://csp-ssl.picsearch.com/img/i/T/l/k/image_iTlk3U9nLHF-5bn78WcjoQ/1.jpg"><span class="video-play-icon"></span><span class="slick-bg-layer"></span></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/be650aad-5fef-4343-8557-c6405e0d0f79-1489354353.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/67bedf7d-d6d3-405a-bc90-8903c1be2082-1489354247.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1daa098e-7286-4b00-b6f8-4ca9e5806f91-1489354228.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/847b7311-a8cf-4986-a961-33497268bf80-1489354298.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d0291975-36c8-4a7b-bccd-2325f83895e2-1489354271.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/89add1d4-966c-481b-88c8-512814b71ade-1489354332.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b5357ed2-9b12-4d82-9e8c-75670f9dbb8f-1469057670.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/280e7fb0-d4de-4255-bb80-9bdb1948e5c8-1469057538.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f7eb2244-8023-4f81-996b-2e7da4155bca-1469057577.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4dccc3c1-4726-4bb8-84bd-ec939c954f0f-1469057597.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2d3383ec-6079-46ff-9c8c-a0905fbf6584-1469057554.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-11" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4738df3f-0d0c-47ae-a88e-2bb1b0d616e9-1469057572.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-12" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2c45fd6f-91d4-4fba-954a-edb1ecba23c7-1480200246.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/0b499c00-ccce-42c0-8164-d73d35563bce-1469057690.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-14" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ba5a76bb-e974-443b-8f8a-e7d9ad8e9e68-1469057745.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-15" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a0013756-2796-4f08-9a6b-470319b54a01-1489354259.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="is24-ex-video"><img alt="Videobild" class="block horizontal-center" id="listing-7-slide-16" data-video-id="iTlk3U9nLHF-5bn78WcjoQ" style="max-height:100%;max-width:100%;margin:auto;position:absolute;top:0;bottom:0;left:0;right:0" src="https://csp-ssl.picsearch.com/img/i/T/l/k/image_iTlk3U9nLHF-5bn78WcjoQ/1.jpg"><span class="video-play-icon"></span><span class="slick-bg-layer"></span></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/be650aad-5fef-4343-8557-c6405e0d0f79-1489354353.png/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="18" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/67bedf7d-d6d3-405a-bc90-8903c1be2082-1489354247.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="19" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1daa098e-7286-4b00-b6f8-4ca9e5806f91-1489354228.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="20" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/847b7311-a8cf-4986-a961-33497268bf80-1489354298.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="21" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d0291975-36c8-4a7b-bccd-2325f83895e2-1489354271.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="22" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/89add1d4-966c-481b-88c8-512814b71ade-1489354332.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="23" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b5357ed2-9b12-4d82-9e8c-75670f9dbb8f-1469057670.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="24" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/280e7fb0-d4de-4255-bb80-9bdb1948e5c8-1469057538.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="25" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f7eb2244-8023-4f81-996b-2e7da4155bca-1469057577.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="26" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4dccc3c1-4726-4bb8-84bd-ec939c954f0f-1469057597.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="27" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2d3383ec-6079-46ff-9c8c-a0905fbf6584-1469057554.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="28" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-11" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4738df3f-0d0c-47ae-a88e-2bb1b0d616e9-1469057572.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="29" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-12" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2c45fd6f-91d4-4fba-954a-edb1ecba23c7-1480200246.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="30" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-13" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/0b499c00-ccce-42c0-8164-d73d35563bce-1469057690.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="31" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-14" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/ba5a76bb-e974-443b-8f8a-e7d9ad8e9e68-1469057745.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="32" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-7-slide-15" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a0013756-2796-4f08-9a6b-470319b54a01-1489354259.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="33" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="is24-ex-video"><img alt="Videobild" class="block horizontal-center" id="listing-7-slide-16" data-video-id="iTlk3U9nLHF-5bn78WcjoQ" style="max-height:100%;max-width:100%;margin:auto;position:absolute;top:0;bottom:0;left:0;right:0" src="https://csp-ssl.picsearch.com/img/i/T/l/k/image_iTlk3U9nLHF-5bn78WcjoQ/1.jpg"><span class="video-play-icon"></span><span class="slick-bg-layer"></span></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">17</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="result-list-entry__linkable-criteria padding-top-m palm-hide"><span class="with-icon"><i class="s24-icons-s24_movie_24"></i><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="is24-ex-video" class="margin-right-s with-icon">Video</a></span></div><div class="small-listings--realtor-logo-container"><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/b9800be2-5c4a-429c-9aa8-c41f65e2db52.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge maxtwolinerHeadline font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Ruhige und günstige 3-ZKB Dachgeschosswohnung, 2-er WG geeignet</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">4.91 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="129475294" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Jägerschneise 4, Linden, Gießen (Kreis)</button></div></div><div class="result-list-entry__criteria"><a href="/expose/129475294" data-go-to-expose-id="129475294"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">680 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">80 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Garten</li><li class="margin-top-none margin-bottom-xs">...</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/129475294" data-go-to-expose-id="129475294" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/b9800be2-5c4a-429c-9aa8-c41f65e2db52.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/129475294" data-go-to-expose-id="129475294" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Ihr Vermietungsteam der Sucasa </span><span class="font-ellipsis">sucasa e.K.</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.12607949" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="align-center contentbanner_11 ad-placeholder"><s24-ad-slot class="is24-adplace align-center" ad-unit-path="/4467/IS24_DE/resultlist/contentbanner_11" id="contentbanner_11" data-viewmode="LIST" aria-hidden="true" preload="350" ad-label-center="true" ad-label-text="Anzeige" ad-label-top="true" size-map-0x0="300x250,320x100,320x240,320x400,fluid" size-map-468x0="300x250,320x100,320x240,320x400,fluid" size-map-728x0="300x250,320x240,680x220,320x400,fluid" size-map-776x0="300x250,320x240,680x220,730x400,fluid" size-map-848x0="300x250,320x240,680x220,800x250,730x400,fluid" size-map-997x0="300x250,320x240,680x220,730x400,fluid" size-map-1048x0="680x220,730x400,fluid" size-map-1120x0="800x250,680x220,730x400,fluid"></s24-ad-slot></li><li class="result-list__listing " data-id="113185270"><article data-item="result" data-obid="113185270" id="result-l-113185270" class="result-list-entry result-list-entry--m false" data-listing-size="M" aria-label="listing-M"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 2527px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-8-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fffe1b93-7049-4a87-8d38-5cc0cd4ae1ac-1315135263.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-8-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/7b097051-f963-4c34-9848-f5f4437294e4-1315134339.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-8-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/6934722c-0535-479e-88c1-3c1e56f290d5-1315134341.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-8-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fffe1b93-7049-4a87-8d38-5cc0cd4ae1ac-1315135263.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-8-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/7b097051-f963-4c34-9848-f5f4437294e4-1315134339.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-8-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/6934722c-0535-479e-88c1-3c1e56f290d5-1315134341.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-8-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fffe1b93-7049-4a87-8d38-5cc0cd4ae1ac-1315135263.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">3</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/e38fe9f9-ce6a-4096-a922-19cdcd451bd7.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>2 Zimmerwohnung, Uni-nah</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">0.46 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="113185270" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Stephanstraße 23, Innenstadt, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/113185270" data-go-to-expose-id="113185270"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">540 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">56,75 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Keller</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/113185270" data-go-to-expose-id="113185270" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/e38fe9f9-ce6a-4096-a922-19cdcd451bd7.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/113185270" data-go-to-expose-id="113185270" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Frau Cornelia  Wallenfels</span><span class="font-ellipsis">Lang GmbH &amp; Co. KG</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.5377865" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147616510"><article data-item="result" data-obid="147616510" id="result-l-147616510" class="result-list-entry result-list-entry--m false" data-listing-size="M" aria-label="listing-M"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 4693px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/40480a0d-ba53-4db0-bde2-65b0b372d3a1-1681897125.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9806e768-d3ba-452a-83fe-aa059dae2616-1681897145.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2bc34587-5be3-4803-8e20-d4f2ed2e4a21-1681897104.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d509d1b2-a9ab-46a6-84df-23ae06001af7-1681897142.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bb83871e-6e55-4bd0-8938-7a671ff4221a-1681897098.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/028738e9-4052-43b1-bccc-4bddb7cf582a-1681897102.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/40480a0d-ba53-4db0-bde2-65b0b372d3a1-1681897125.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9806e768-d3ba-452a-83fe-aa059dae2616-1681897145.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2bc34587-5be3-4803-8e20-d4f2ed2e4a21-1681897104.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d509d1b2-a9ab-46a6-84df-23ae06001af7-1681897142.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bb83871e-6e55-4bd0-8938-7a671ff4221a-1681897098.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/028738e9-4052-43b1-bccc-4bddb7cf582a-1681897102.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-9-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/40480a0d-ba53-4db0-bde2-65b0b372d3a1-1681897125.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">6</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/ce57c77c-2ddf-485d-9650-f006b1803ab4.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Erstbezug im Herzen Gießens</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">0.54 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147616510" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Walltorstraße 16, Innenstadt, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147616510" data-go-to-expose-id="147616510"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">739 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">57 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">WG-geeignet</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147616510" data-go-to-expose-id="147616510" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/ce57c77c-2ddf-485d-9650-f006b1803ab4.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/147616510" data-go-to-expose-id="147616510" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Frau Lea Burk</span><span class="font-ellipsis">Real Estate Service Hartmann &amp; Burk GbR</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="002.01009270899" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147638484"><article data-item="result" data-obid="147638484" id="result-l-147638484" class="result-list-entry result-list-entry--m false" data-listing-size="M" aria-label="listing-M"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 4693px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1295d25b-e2ad-4b16-9943-a2795d395eb2-1682610869.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fcda86a7-125b-4b37-bf53-2411d369ced6-1682610295.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fe514e92-231e-4375-af9d-ad723f558455-1682610914.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4c60c06a-f4a9-472f-8324-552620d2e2ad-1682610882.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/019ae2d2-af19-423f-ac2c-edac5418c979-1682610953.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b5ed70f8-6da3-4731-94b4-8f8df81e3104-1682610945.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1295d25b-e2ad-4b16-9943-a2795d395eb2-1682610869.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fcda86a7-125b-4b37-bf53-2411d369ced6-1682610295.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/fe514e92-231e-4375-af9d-ad723f558455-1682610914.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4c60c06a-f4a9-472f-8324-552620d2e2ad-1682610882.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/019ae2d2-af19-423f-ac2c-edac5418c979-1682610953.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b5ed70f8-6da3-4731-94b4-8f8df81e3104-1682610945.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-10-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1295d25b-e2ad-4b16-9943-a2795d395eb2-1682610869.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">6</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/3fdc9491-128d-4f68-a5a0-59cdca908f76.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Frisch sanierte 2,5-Zimmer-Wohnung in Gießen</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">0.56 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147638484" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Lessingstraße 4, Innenstadt, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147638484" data-go-to-expose-id="147638484"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">535 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">53,93 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Keller</li><li class="margin-top-none margin-bottom-xs">WG-geeignet</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147638484" data-go-to-expose-id="147638484" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/3fdc9491-128d-4f68-a5a0-59cdca908f76.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/147638484" data-go-to-expose-id="147638484" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Frau Evelina Drobik</span><span class="font-ellipsis">WEVATO GmbH</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="002.01005507036" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="126716839"><article data-item="result" data-obid="126716839" id="result-l-126716839" class="result-list-entry result-list-entry--m false" data-listing-size="M" aria-label="listing-M"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 5415px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2cb4ae5e-147d-45f5-9524-ac829f6afda9-1683957218.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1390a2a1-04a7-4036-9817-3b2063cbbdba-1429775907.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c9f93788-fb97-4b4f-91f9-fa07ecd49a96-1429775949.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/664ef5b6-02a4-4dc4-bf5c-7fa9a4b8a723-1683957351.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/695ce2d7-d644-4482-9752-82bdb6812f19-1683957425.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1b2c34c9-f6ce-40ed-88ec-649239d2c3de-1683957211.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/7382087d-ba72-4db8-88ec-36b1003a872a-1683957213.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2cb4ae5e-147d-45f5-9524-ac829f6afda9-1683957218.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1390a2a1-04a7-4036-9817-3b2063cbbdba-1429775907.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c9f93788-fb97-4b4f-91f9-fa07ecd49a96-1429775949.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/664ef5b6-02a4-4dc4-bf5c-7fa9a4b8a723-1683957351.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/695ce2d7-d644-4482-9752-82bdb6812f19-1683957425.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1b2c34c9-f6ce-40ed-88ec-649239d2c3de-1683957211.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/7382087d-ba72-4db8-88ec-36b1003a872a-1683957213.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-11-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2cb4ae5e-147d-45f5-9524-ac829f6afda9-1683957218.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">7</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="result-list-entry__linkable-criteria padding-top-m palm-hide"><span class="with-icon"><i class="s24-icons-s24_floor_plan_24"></i><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="is24-ex-floorplans" class="margin-right-s with-icon">Grundriss</a></span></div><div class="small-listings--realtor-logo-container"></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/126716839" data-go-to-expose-id="126716839" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Neubau am Kugelberg in Gießen - hier: Penthouse 2 Zi. Whg. mit Dachterrasse und Wohnküche, inkl. EBK</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">1.08 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="126716839" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Lärchenwäldchen 7, Gießen-Ost, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/126716839" data-go-to-expose-id="126716839"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">583 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">45,19 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Keller</li><li class="margin-top-none margin-bottom-xs">...</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item one-third font-ellipsis"><a href="/expose/126716839" data-go-to-expose-id="126716839" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Frau Judith Radtke IBG Immobilienbetreuung GmbH </span><span class="font-ellipsis">FIVE STAR Investment GmbH</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="002.01010007243" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147308685"><article data-item="result" data-obid="147308685" id="result-l-147308685" class="result-list-entry result-list-entry--m false" data-listing-size="M" aria-label="listing-M"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 8303px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c3bf7ba8-be41-4a65-8f24-847291714ae1-1673892485.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2e4dccba-5e7d-4d1a-81bb-b9305cc1a161-1673892425.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f79a089d-83c2-48dc-b483-dc86805bbadf-1673892427.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c176b4a0-a63e-4597-ae93-8d65b3505218-1673892431.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1b3715b8-ef75-4b26-ac68-3c4585639105-1673892434.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a9f88506-7a6a-4e24-bdef-4a261318c71d-1673892440.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/43bbf722-1b6d-4a47-a130-44fbce06da2a-1673892445.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1d63383c-7379-467b-ae78-f90c36c78bb6-1673892453.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/6e66e79b-29d6-46fb-8d22-b5352a409fda-1673892461.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b5904879-4a7a-400b-be81-4ed79cffc8d1-1673892471.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1edbb5c9-4be3-43cd-9642-8613b12849b6-1673892480.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c3bf7ba8-be41-4a65-8f24-847291714ae1-1673892485.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2e4dccba-5e7d-4d1a-81bb-b9305cc1a161-1673892425.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/f79a089d-83c2-48dc-b483-dc86805bbadf-1673892427.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c176b4a0-a63e-4597-ae93-8d65b3505218-1673892431.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1b3715b8-ef75-4b26-ac68-3c4585639105-1673892434.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a9f88506-7a6a-4e24-bdef-4a261318c71d-1673892440.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/43bbf722-1b6d-4a47-a130-44fbce06da2a-1673892445.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1d63383c-7379-467b-ae78-f90c36c78bb6-1673892453.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="18" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/6e66e79b-29d6-46fb-8d22-b5352a409fda-1673892461.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="19" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b5904879-4a7a-400b-be81-4ed79cffc8d1-1673892471.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="20" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1edbb5c9-4be3-43cd-9642-8613b12849b6-1673892480.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="21" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-12-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/c3bf7ba8-be41-4a65-8f24-847291714ae1-1673892485.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">11</span></div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/fc2f3c51-6bcf-4e3d-8bac-b308b3b28d7b.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths">Moderne Dachgeschosswohnung in zentraler Lage</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">2.9 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147308685" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Eisenstein 4, Wieseck, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147308685" data-go-to-expose-id="147308685"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">800 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">68 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147308685" data-go-to-expose-id="147308685" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/fc2f3c51-6bcf-4e3d-8bac-b308b3b28d7b.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/147308685" data-go-to-expose-id="147308685" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Herr Mike Biehl</span><span class="font-ellipsis">Kirchmann Immobilienvermittlung GmbH</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="002.01008207922" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="align-center contentbanner_17 ad-placeholder"><s24-ad-slot class="is24-adplace align-center" ad-unit-path="/4467/IS24_DE/resultlist/contentbanner_17" id="contentbanner_17" data-viewmode="LIST" aria-hidden="true" preload="350" ad-label-center="true" ad-label-text="Anzeige" ad-label-top="true" size-map-0x0="300x250,320x100,320x240,320x400,fluid" size-map-468x0="300x250,320x100,320x240,468x60,320x400,fluid" size-map-728x0="300x250,320x240,468x60,680x220,320x400,fluid" size-map-776x0="300x250,320x240,468x60,680x220,728x90,730x400,fluid" size-map-848x0="300x250,320x240,468x60,680x220,728x90,800x250,730x400,fluid" size-map-997x0="300x250,320x240,468x60,680x220,730x400,fluid" size-map-1048x0="680x220,728x90,730x400,fluid" size-map-1120x0="800x250,680x220,728x90,730x400,fluid"></s24-ad-slot></li><li class="result-list__listing " data-id="136625278"><article data-item="result" data-obid="136625278" id="result-l-136625278" class="result-list-entry result-list-entry--m false" data-listing-size="M" aria-label="listing-M"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><div class="slick-slider slick-initialized" dir="ltr"><button class="slick-arrow slick-prev s24-icons-s24_chevron_left_24"></button><div class="slick-list"><div class="slick-track" style="width: 8303px; opacity: 1; transform: translate3d(-361px, 0px, 0px);"><div data-index="-1" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/43b5e90a-9bf2-4660-ade3-aa9c5317fe6e-1561999802.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/404be2ab-0c07-4178-8f05-4ef4a7ce76c9-1561999748.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="1" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1c17fbb0-0402-4713-8f63-160dbe281db2-1561999754.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="2" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/71c87f8d-4ae2-4c82-83ce-98f724f42652-1561999758.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="3" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bc4ed4db-17ca-4541-b273-68b89c222448-1561999764.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="4" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2050e659-e4a0-4395-933e-26f529659df9-1561999769.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="5" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9ac85264-c712-4d92-92fd-d8fa8d7929ad-1561999776.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="6" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/454522e8-c415-436f-ab54-797563a3cc0a-1561999784.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="7" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bad6f180-8e03-492a-8724-513c1533a548-1561999789.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="8" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a53b08bc-c2aa-4fd4-8b1e-7c7586f9eff4-1561999795.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="9" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d6d9e10c-a981-4c35-a9c7-6b1cd8f6c3af-1561999798.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="10" class="slick-slide" tabindex="-1" aria-hidden="true" style="outline: none; width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/43b5e90a-9bf2-4660-ade3-aa9c5317fe6e-1561999802.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="11" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/404be2ab-0c07-4178-8f05-4ef4a7ce76c9-1561999748.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="12" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-1" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/1c17fbb0-0402-4713-8f63-160dbe281db2-1561999754.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="13" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-2" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/71c87f8d-4ae2-4c82-83ce-98f724f42652-1561999758.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="14" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-3" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bc4ed4db-17ca-4541-b273-68b89c222448-1561999764.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="15" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-4" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/2050e659-e4a0-4395-933e-26f529659df9-1561999769.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="16" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-5" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/9ac85264-c712-4d92-92fd-d8fa8d7929ad-1561999776.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="17" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-6" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/454522e8-c415-436f-ab54-797563a3cc0a-1561999784.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="18" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-7" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bad6f180-8e03-492a-8724-513c1533a548-1561999789.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="19" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-8" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/a53b08bc-c2aa-4fd4-8b1e-7c7586f9eff4-1561999795.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="20" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-9" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d6d9e10c-a981-4c35-a9c7-6b1cd8f6c3af-1561999798.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div><div data-index="21" tabindex="-1" class="slick-slide slick-cloned" aria-hidden="true" style="width: 361px;"><div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-13-slide-10" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/43b5e90a-9bf2-4660-ade3-aa9c5317fe6e-1561999802.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a></div></div></div></div><button class="slick-arrow slick-next s24-icons-s24_chevron_right_24"></button></div><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><span class="image-index-label">1</span><span>/</span><span class="total-media-count-label">11</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="result-list-entry__linkable-criteria padding-top-m palm-hide"><span class="with-icon"><i class="s24-icons-s24_floor_plan_24"></i><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="is24-ex-floorplans" class="margin-right-s with-icon">Grundriss</a></span></div><div class="small-listings--realtor-logo-container"><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/fc2f3c51-6bcf-4e3d-8bac-b308b3b28d7b.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Moderne 2-Zimmer-Wohnung mit Balkon</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">3.1 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="136625278" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Fockestraße 2, Gießen-Ost, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/136625278" data-go-to-expose-id="136625278"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">770 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">64 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Aufzug</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/136625278" data-go-to-expose-id="136625278" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--realtor vertical-center-container"><img alt="Anbieterlogo" class="result-list-entry__brand-logo vertical-center lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/usercontent/fc2f3c51-6bcf-4e3d-8bac-b308b3b28d7b.JPG/ORIG/resize/120x50%3E/quality/80"></div></a></div><div class="grid-item one-third font-ellipsis"><a href="/expose/136625278" data-go-to-expose-id="136625278" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Herr Mike Biehl</span><span class="font-ellipsis">Kirchmann Immobilienvermittlung GmbH</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="002.01008207922" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147637654"><article data-item="result" data-obid="147637654" id="result-l-147637654" class="result-list-entry result-list-entry--s paywall-listing" data-listing-size="S" aria-label="listing-S"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="palm-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><a href="/expose/147637654" data-go-to-expose-id="147637654" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-14-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/0d5cc572-8c3b-443a-b034-f3b1b470567b-1682587046.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><i class="s24-icons-s24_picture_24 margin-right-xs" style="vertical-align:text-bottom;font-size:15px"></i><span class="total-media-count-label">10</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147637654" data-go-to-expose-id="147637654" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="desk-hide lap-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147637654" data-go-to-expose-id="147637654" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Zwischenmiete! Für 3 Monate in geräumiger Wohnung mit guter Lage</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147637654" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Innenstadt, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147637654" data-go-to-expose-id="147637654"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">600 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">59 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2,5<!-- --> Zi.</span><span class="onlyLarge">2,5</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Garten</li><li class="margin-top-none margin-bottom-xs">Keller</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147637654" data-go-to-expose-id="147637654" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div><div class="grid-item one-third font-ellipsis"></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.20618702" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="146396243"><article data-item="result" data-obid="146396243" id="result-l-146396243" class="result-list-entry result-list-entry--s false" data-listing-size="S" aria-label="listing-S"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><a href="/expose/146396243" data-go-to-expose-id="146396243" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-15-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/3fd42eea-ab9a-4333-b679-27d9f1857d54-1675969201.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><i class="s24-icons-s24_picture_24 margin-right-xs" style="vertical-align:text-bottom;font-size:15px"></i><span class="total-media-count-label">6</span></div></div></div></div><div class="small-listings--realtor-logo-container"></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/146396243" data-go-to-expose-id="146396243" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths">Sanierte Dachterrassenwohnung im 2 Fam. Haus / Anneröder Siedlung</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="146396243" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Gießen-Ost, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/146396243" data-go-to-expose-id="146396243"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">695 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">81 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item one-third font-ellipsis"><a href="/expose/146396243" data-go-to-expose-id="146396243" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Herr Stefan Sahl</span><span class="font-ellipsis">Stefan Sahl Immobilien</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.503799" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147659700"><article data-item="result" data-obid="147659700" id="result-l-147659700" class="result-list-entry result-list-entry--s paywall-listing" data-listing-size="S" aria-label="listing-S"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="palm-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><a href="/expose/147659700" data-go-to-expose-id="147659700" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-16-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/4299e752-ec0d-428c-824a-6da79203a44d-1683559293.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><i class="s24-icons-s24_picture_24 margin-right-xs" style="vertical-align:text-bottom;font-size:15px"></i><span class="total-media-count-label">8</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147659700" data-go-to-expose-id="147659700" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="desk-hide lap-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147659700" data-go-to-expose-id="147659700" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>2-Zimmer-EG-Wohnung mit Balkon und Einbauküche in Gießen</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">2.22 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147659700" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Heinrich-Ritzel-Straße 2, Wieseck, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147659700" data-go-to-expose-id="147659700"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">550 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">44 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Garten</li><li class="margin-top-none margin-bottom-xs">...</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147659700" data-go-to-expose-id="147659700" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div><div class="grid-item one-third font-ellipsis"></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.20537015" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147283283"><article data-item="result" data-obid="147283283" id="result-l-147283283" class="result-list-entry result-list-entry--s false" data-listing-size="S" aria-label="listing-S"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><a href="/expose/147283283" data-go-to-expose-id="147283283" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-17-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/d9ea8fea-1d31-4fd8-80db-f0d6ab9386fb-1673189724.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><i class="s24-icons-s24_picture_24 margin-right-xs" style="vertical-align:text-bottom;font-size:15px"></i><span class="total-media-count-label">19</span></div></div></div></div><div class="small-listings--realtor-logo-container"></div></div><div class="grid-item desk-hide lap-hide one-whole"></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147283283" data-go-to-expose-id="147283283" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths">Helle freundliche 3 ZKB Wohnung mit Küchenzeile (1501-5016)</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"><div class="margin-right-xs">2.59 km |</div></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147283283" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Ludwig-Schneider-Weg 1-7, Gießen-West, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147283283" data-go-to-expose-id="147283283"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">800 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">87 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Einbauküche</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item one-third font-ellipsis"><a href="/expose/147283283" data-go-to-expose-id="147283283" target="_self" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="font-s undefined" data-event="evtrack" data-tracking="{
          &quot;evt_ga_category&quot;: &quot;commercial&quot;,
          &quot;evt_ga_action&quot;: &quot;contact_realtor&quot;,
          &quot;evt_ga_label&quot;: &quot;mail_intent_agent_name&quot;,
          &quot;ns_type&quot;: &quot;hidden&quot;
         }"><span class="font-ellipsis">Sandra Schäfer</span><span class="font-ellipsis">Finas GmbH &amp; Co. KG</span></a></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.5361688" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="align-center list_content_banner_4 ad-placeholder"><s24-ad-slot class="is24-adplace align-center" ad-unit-path="/4467/IS24_DE/resultlist/list_content_banner_4" id="list_content_banner_4" data-viewmode="LIST" aria-hidden="true" preload="350" ad-label-center="true" ad-label-text="Anzeige" ad-label-top="true" size-map-0x0="320x100,fluid" size-map-468x0="320x100,fluid" size-map-728x0="320x100,468x60,fluid" size-map-776x0="728x90,468x60,fluid" size-map-848x0="728x90,468x60,fluid" size-map-997x0="728x90,468x60,fluid" size-map-1048x0="728x90,fluid" size-map-1120x0="728x90,fluid"></s24-ad-slot></li><li class="result-list__listing " data-id="140712013"><article data-item="result" data-obid="140712013" id="result-l-140712013" class="result-list-entry result-list-entry--s paywall-listing" data-listing-size="S" aria-label="listing-S"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="palm-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><a href="/expose/140712013" data-go-to-expose-id="140712013" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-18-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/b5b61b8f-e1e2-4400-b526-b568a5321fec-1674550381.jpg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><i class="s24-icons-s24_picture_24 margin-right-xs" style="vertical-align:text-bottom;font-size:15px"></i><span class="total-media-count-label">4</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/140712013" data-go-to-expose-id="140712013" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="desk-hide lap-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/140712013" data-go-to-expose-id="140712013" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>2-Zimmer-Wohnung mit Balkon in Giessen-Wieseck</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="140712013" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Wieseck, Gießen</button></div></div><div class="result-list-entry__criteria"><a href="/expose/140712013" data-go-to-expose-id="140712013"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">480 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">46 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">2<!-- --> Zi.</span><span class="onlyLarge">2</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Balkon/Terrasse</li><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Keller</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/140712013" data-go-to-expose-id="140712013" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div><div class="grid-item one-third font-ellipsis"></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="001.19742205" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li><li class="result-list__listing " data-id="147470506"><article data-item="result" data-obid="147470506" id="result-l-147470506" class="result-list-entry result-list-entry--s paywall-listing" data-listing-size="S" aria-label="listing-S"><div class="grid grid-flex"><div class="grid-item result-list-entry__gallery-container" aria-hidden="true"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="palm-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span><div class="gallery-responsive" data-testid="gallery"><div style="padding-top:75%"></div><div class="gallery-container loading"><a href="/expose/147470506" data-go-to-expose-id="147470506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius"><span class="slick-bg-layer"></span><img alt="Immobilienbild" id="listing-19-slide-0" width="420" height="315" class="gallery__image block height-full lazyImage" src="//www.static-immobilienscout24.de/statpic/search/71a50dbba44c78128b221b7df7bb51f1_1x1.png" data-lazy-src="https://pictures.immobilienscout24.de/listings/bd1e5811-d931-4475-a8d0-e6a9f8902d5f-1677894286.jpeg/ORIG/legacy_thumbnail/420x315/format/webp/quality/73"></a><div class="gallery__count-new-container"><div data-testid="gallery-media-count" class="gallery__count"><i class="s24-icons-s24_picture_24 margin-right-xs" style="vertical-align:text-bottom;font-size:15px"></i><span class="total-media-count-label">9</span></div><div class="result-list-entry__new-flag">NEU</div></div></div></div><div class="small-listings--realtor-logo-container"><a href="/expose/147470506" data-go-to-expose-id="147470506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div></div><div class="grid-item desk-hide lap-hide one-whole"><span data-testid="link-to-modal" class="is24-pointer" role="button" tabindex="0"><div class="desk-hide lap-hide lfl-info plusBooking"><div class="vertical-center-container"><span class="vertical-highlighter vertical-center margin-right-s"></span><span class="vertical-center">Nur exklusiv für <div class="inline-block"><span class="underline-highlighter-kplus font-normal">Mieter</span><span class="plus-highlighter font-bold">Plus</span></div></span><i class="s24-icons-s24_info_circle_24 font-xl margin-left align-middle" role="button" tabindex="0"></i></div></div></span></div><div class="grid-item result-list-entry__data-container"><div class="result-list-entry__data"><div class="result-list-entry__shortlist-star type-normal"><button aria-label="Zum Merkzettel hinzufügen" class="button-reset shortlist-star s24-icons-s24_heart_24"></button></div><div class="more-options-control"><button aria-label="Mehr Optionen" class="button-reset result-list-entry__more-button type-normal"><i class="s24-icons-s24_menu_sub_24" style="font-size:24px"></i></button></div><a href="/expose/147470506" data-go-to-expose-id="147470506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" class="result-list-entry__brand-title-container "><h2 class="result-list-entry__brand-title font-h6 onlyLarge font-ellipsis font-regular nine-tenths"><span class="result-list-entry__new-flag margin-right-xs">NEU</span>Schöne 3-Zimmer-Wohnung zur Miete in 35435, Wettenberg</h2></a><div class="nine-tenths margin-top-m"><div class="float-left"></div><div class="result-list-entry__address"><button title="Auf der Karte anzeigen" data-result-id="147470506" class="result-list-entry__map-link link-text-secondary font-normal font-ellipsis"><span class="s24-icons-s24_location_pin_1_24 result-list-entry__map-link__icon inline-block margin-right-xs"></span>Wettenberg, Gießen (Kreis)</button></div></div><div class="result-list-entry__criteria"><a href="/expose/147470506" data-go-to-expose-id="147470506"><div class="grid grid-flex gutter-horizontal-l gutter-vertical-s" data-is24-qa="attributes"><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">800 €</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Kaltmiete</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular">95 m²</dd><dt class="font-tabular onlyLarge font-xs attribute-label">Wohnfläche</dt></dl><dl class="grid-item result-list-entry__primary-criterion " role="presentation"><dd class="font-highlight font-tabular"><span><span class="onlySmall">3<!-- --> Zi.</span><span class="onlyLarge">3</span></span></dd><dt class="font-tabular onlyLarge font-xs attribute-label"><abbr title="Zimmer">Zi.</abbr></dt></dl></div></a><div class="result-list-entry__secondary-criteria-container font-s margin-top-m"><ul class="result-list-entry__secondary-criteria" role="presentation"><li class="margin-top-none margin-bottom-xs">Einbauküche</li><li class="margin-top-none margin-bottom-xs">Keller</li></ul></div></div><div class="result-list-entry__realtor-data-container padding-top-s margin-top-m"><div class="result-list-entry__realtor-data"><div class="grid flex-nowrap grid-flex grid-fill-rows  gutter-m"><div class="grid-item grid-item-fixed-width"><a href="/expose/147470506" data-go-to-expose-id="147470506" data-go-to-expose-referrer="RESULT_LIST_LISTING" data-go-to-expose-searchtype="radius" data-go-to-expose-hash="/basicContact" class="result-list-entry__brand-logo-container"><div class="result-list-entry__brand-logo--private"></div></a></div><div class="grid-item one-third font-ellipsis"></div><div class="grid-item grid-item-fixed-width"><span data-entry-cwid="009.1abb5c94-cf4a-4f13-8cc8-c434c66778a3" data-testid="realtor-ev-placeholder"></span></div></div></div></div></div></div></div></article></li></ul><div class="align-center" data-testid="pager"><ul class="reactPagination"><li class="p-items p-prev vertical-center-container disabled"><a class=" " tabindex="-1" role="button" aria-disabled="true" aria-label="Previous page" rel="prev"><span class="p-arrow s24-icons-s24_chevron_left_24 vertical-center"></span></a></li><li class="p-items p-active"><a rel="canonical" role="button" tabindex="-1" aria-label="Page 1 is your current page" aria-current="page">1</a></li><li class="p-items"><a rel="next" role="button" tabindex="0" aria-label="Page 2">2</a></li><li class="p-items p-next vertical-center-container"><a class="" tabindex="0" role="button" aria-disabled="false" aria-label="Next page" rel="next"><span class="p-arrow s24-icons-s24_chevron_right_24 vertical-center"></span></a></li></ul></div><span data-qa="feature-switches" data-feature-switches-synced="false"></span></div></div><div class="listings-content-area__sidebar grid-item palm-hide lap-hide desk-margin-left-m"><div id="sidebar"><div class="sidebar-teaser-collection-box margin-bottom-xl border-bottom padding-l background-sidebar font-s"><div class="touchpoint-space"><div data-testid="resultlist-touchpoint"><div class="touchpoint-touchpoint__touchpoint--1wqE6"><div class="grid grid-flex grid-fill-rows"><div class="grid-item palm-hide lap-hide one-whole"><section><div class="touchpoint-touchpoint__touchpointTitle--3ehZz font-h6">Immobilien­vermarktung vom Profi</div></section><div class="touchpoint-touchpoint__touchpointSeparator--1PVbt"></div></div><div class="grid-item palm-order-two-up lap-order-two-up one-whole"><div class="touchpoint-brandBar__bar--3Y_Jm" style="background-color: rgb(52, 52, 52);"></div></div><div class="grid-item palm-order-two-down desk-one-whole touchpoint-touchpoint__touchpointRealtorPicture--1WVCE"><div class="touchpoint-touchpoint__touchpointPictureContainer--2ep8v"><div class="touchpoint-profileImage__container--1Hd8p undefined"><a class="touchpoint-profileImage__link--1d5bW" href="/anbieter/profil/claus-r-menges-gmbh-immobilienvermittlung-und-hausverwaltung?contactReason=WANT_TO_LEASE&amp;referer=standard&amp;cmp_id=10-04358&amp;cmp_name=residential_realtordirectory&amp;cmp_position=residential_resultlist&amp;cmp_creative=touchpoint_standard_065310050600_001.17215" target="_blank"><img class="touchpoint-profileImage__image--1iA0M " src="https://pictures.immobilienscout24.de/usercontent/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG/ORIG/legacy_thumbnail/252x252/format/jpg/quality/90" srcset="https://pictures.immobilienscout24.de/usercontent/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG/ORIG/legacy_thumbnail/252x252/format/jpg/quality/90,
      https://pictures.immobilienscout24.de/usercontent/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG/ORIG/legacy_thumbnail/504x504/format/jpg/quality/90 2x,
      https://pictures.immobilienscout24.de/usercontent/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG/ORIG/legacy_thumbnail/756x756/format/jpg/quality/90 3x" title="Claus R. Menges GmbH" alt="Claus R. Menges GmbH"><div class="touchpoint-profileImage__touchpointBadgeStandard_immoExpert--2S4dM"></div></a></div></div></div><div class="grid-item desk-one-whole touchpoint-touchpoint__touchpointMiddleSection--1yBYg"><div class="touchpoint-touchpoint__touchpointTitle--3ehZz desk-hide font-h6">Immobilien­vermarktung vom Profi</div><div class="touchpoint-touchpoint__touchpointSeparator--1PVbt desk-hide"></div><div class="touchpoint-touchpoint__touchpointRealtorName--7d2FC"><div><a target="_blank" href="/anbieter/profil/claus-r-menges-gmbh-immobilienvermittlung-und-hausverwaltung?contactReason=WANT_TO_LEASE&amp;referer=standard&amp;cmp_id=10-04358&amp;cmp_name=residential_realtordirectory&amp;cmp_position=residential_resultlist&amp;cmp_creative=touchpoint_standard_065310050600_001.17215">Claus R. Menges GmbH</a> versteht Ihre Bedürfnisse und bietet eine optimale Vermarktung Ihrer Wohnung in Ihrer Region</div></div></div><div class="grid-item palm-one-whole desk-one-whole palm-order-two-down lap-order-two-down touchpoint-touchpoint__touchpointBottomSection--2Qt_q"><div class="grid grid-flex"><div class="grid-item palm-one-half lap-one-whole desk-one-whole"><a target="_blank" aria-label="Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung"><img class="touchpoint-companyLogo__logo--2scoq" src="https://pictures.immobilienscout24.de/usercontent/3efdac24-295f-4267-9ce5-a3e710345539.PNG/ORIG/resize/120x120/format/png" srcset="https://pictures.immobilienscout24.de/usercontent/3efdac24-295f-4267-9ce5-a3e710345539.PNG/ORIG/resize/120x120/format/png,
      https://pictures.immobilienscout24.de/usercontent/3efdac24-295f-4267-9ce5-a3e710345539.PNG/ORIG/resize/240x240/format/png 2x,
      https://pictures.immobilienscout24.de/usercontent/3efdac24-295f-4267-9ce5-a3e710345539.PNG/ORIG/resize/360x360/format/png 3x" alt="Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung"></a></div><div class="grid-item palm-one-half lap-one-whole desk-one-whole touchpoint-touchpoint__touchpointButtonContainer--2zpEe"><div class="desk-hide palm-hide"></div><a href="/anbieter/profil/claus-r-menges-gmbh-immobilienvermittlung-und-hausverwaltung?contactReason=WANT_TO_LEASE&amp;referer=standard&amp;cmp_id=10-04358&amp;cmp_name=residential_realtordirectory&amp;cmp_position=residential_resultlist&amp;cmp_creative=touchpoint_standard_065310050600_001.17215" class="palm-hide lap-hide one-whole button-secondary touchpoint-touchpoint__touchpointButton--p4y1O">Jetzt kontaktieren</a><a href="/anbieter/profil/claus-r-menges-gmbh-immobilienvermittlung-und-hausverwaltung?contactReason=WANT_TO_LEASE&amp;referer=standard&amp;cmp_id=10-04358&amp;cmp_name=residential_realtordirectory&amp;cmp_position=residential_resultlist&amp;cmp_creative=touchpoint_standard_065310050600_001.17215" class="desk-hide one-whole button touchpoint-touchpoint__touchpointButton--p4y1O">Jetzt kontaktieren</a></div><div class="desk-hide lap-hide"></div></div></div></div></div></div></div><section><h3 class="font-h6"><span class="s24-icons-s24_heart_magnifier_24 font-m vertical-center padding-bottom-xs"></span> Suchalarm</h3><p class="margin-bottom-xs">Bestimme, wann und wie du neue Angebote zu deiner Suche erhältst.</p><a rel="nofollow" href="/Suche/controller/saveSearch.go?reportLabelSaveSearchLocation=contentbox&amp;searchUrl=/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&amp;returnUrl=/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&amp;source=savedsearch" class="icon-arrow block">Suchalarm einrichten</a></section><div data-testid="resultlist-touchpoint"></div><section class="teaser-section"><div class="grid grid-flex grid-justify-center teaser-flex-container"><div class="Indicator_indicator__IhewW Indicator_indicator--brand__4p0ak brand-name margin-bottom-s"><span>Kostenlos vergleichen</span></div><h5 class="align-center margin-bottom-m" data-testid="relocation-teaser-headline">Spare bis zu 42 % beim Umzug</h5><p class="input-hint align-center margin-bottom-s">PLZ deines Wohnorts:</p><div class="teaser-input input-text-container margin-bottom-s palm-margin-bottom-m"><input type="text" data-testid="postal-code-input" class="input-text" placeholder="z. B. 14057"></div><a data-testid="redirection-link" href="/umzug/umzugsunternehmen/vergleichen.html?cmp_id=10-052161&amp;cmp_name=relocation_leadengine&amp;cmp_position=search_resultlist_rent&amp;cmp_creative=sidebar_teaser"><button class="teaser-button margin-bottom-m Button_button__DdOl8" qa-regression-tag="button">Jetzt Preise vergleichen</button></a></div></section></div><s24-ad-slot class="" ad-unit-path="/4467/IS24_DE/resultlist/list_right_banner_2" id="list_right_banner_2" data-viewmode="LIST" aria-hidden="true" preload="150" sticky="default-yes" sticky-lower-bound-selector="#bottomBox" size-map-1014x0="120x600,160x600,200x600,250x500,250x600,fluid" size-map-1163x0="120x600,160x600,200x600,300x250,300x500,300x600,fluid" ad-label-text="Anzeige" ad-label-top="true" ad-label-left="true"></s24-ad-slot></div></div></div><div id="mapContainer" data-with-price-insights-tab="true"><div data-testid="mapLoadingMask" class="border show-only-with-map" style="height:calc(100vh - 17em)"><div class="align-center padding-top-xxl"><div data-testid="loader-spinner" class="loader inline-block align-middle loader-large"></div><div><span>Einen Moment bitte.</span><br><span>Die Karte wird geladen...</span></div></div></div></div><div id="bottomBox"><div data-testid="bottomBox" class="bottom-box margin-top-xl"><div class="grid grid-flex grid-align-baseline gutter-xl"><div class="grid-item palm-one-whole lap-one-whole desk-one-half"><div class="padding-horizontal-s" data-testid="drawSearchLink"><div data-testid="draw_search_link_header_id" class="margin-bottom-s font-semibold link-header">Lege dein Suchgebiet noch individueller fest</div><button class="link-text button-reset font-lightgray" type="button">Jetzt Suchgebiet zeichnen</button></div></div><section data-testid="propertyBookBox" class="grid-item palm-one-whole lap-one-whole desk-one-half"><div class="padding-horizontal-s"><div id="propertyBookLinkHeadline" class="font-semibold margin-bottom-s">Immobilienmarkt und Preise in <!-- -->Gießen</div><a id="propertyBookEntryLink" target="_blank" href="https://atlas.immobilienscout24.de/hierarchy-page-by-id/1276007006005?marketingFocus=APARTMENT_RENT&amp;cmp_id=10-04309&amp;cmp_name=residential_atlas&amp;cmp_position=residential_resultlist&amp;cmp_creative=top_right_info_box_textlink_APARTMENT_RENT#/preis-%C3%BCbersicht" class="block font-lightgray margin-bottom-s">Mehr Immobilienpreise in der Region</a></div></section></div><div class="clearfix"></div><div class="grid grid-flex grid-align-baseline margin-bottom-l"><div class="grid-item palm-one-whole lap-two-thirds desk-two-thirds"><div class="legend hideWhileLoadingEntries"></div></div></div></div></div><div class="list-banner-bottom-placeholder ad-placeholder"><s24-ad-slot class="list-banner-bottom align-center" ad-unit-path="/4467/IS24_DE/resultlist/list_banner_bottom" id="list_banner_bottom" data-viewmode="" aria-hidden="true" preload="100" size-map-0x0="300x250,320x240,fluid" size-map-669x0="300x250,320x240,fluid" size-map-776x0="728x90,fluid" size-map-848x0="800x250,680x220,728x90,fluid" size-map-1018x0="800x250,680x220,728x90,970x250,fluid" ad-label-text="Anzeige" ad-label-top="true" ad-label-center="true"></s24-ad-slot></div><div class="breadcrumb"><span><a class="font-lightgray font-normal margin-horizontal-xs" href="/">Suche</a> › </span><span><a class="font-lightgray font-normal margin-horizontal-xs" href="/Suche/de/hessen/wohnung-mieten">Hessen</a> › </span><span><a class="font-lightgray font-normal margin-horizontal-xs" href="/Suche/de/hessen/giessen-kreis/wohnung-mieten">Gießen (Kreis)</a> › </span><span><a class="font-lightgray font-normal margin-horizontal-xs" href="/Suche/de/hessen/giessen-kreis/giessen/wohnung-mieten">Gießen</a> › </span><span class="font-regular margin-horizontal-xs">Innenstadt</span></div></div><div class="prominent-button-container align-center prominent-button-container-hidden"><button aria-label="Suche speichern. Wenn du nicht angemeldet bist, wirst du auf unsere Login-Seite weitergeleitet." class="button-primary prominent-button font-semibold padding-horizontal-xl" id="saveSearchHeaderLink"><div class="vertical-center-container"><span class="s24-icons-s24_heart_magnifier_24 font-m vertical-center padding-bottom-xs padding-right-xs"></span><span>Suche speichern</span></div></button></div></div><div style="visibility:hidden" class="map-flyout-container "><div class="page-wrapper page-wrapper--full-width absolute-position height-full" role="dialog"><div class="map-flyout-area height-full shadow content-wrapper content-wrapper--palm-stretch"><div class="map-flyout__map-container absolute-reference one-whole height-full"><span class="absolute-content absolute-content--centered font-xxl"><div data-testid="loader-spinner" class="loader inline-block align-middle loader-large"></div></span><button type="button" aria-label="Schließen" class="button-reset cockpit__cockpit-close-icon cockpit__cockpit-close-icon--dark map-flyout__close-icon" title="Schließen"></button></div></div></div></div></div></div>
    
    
  
  









  
  
  
    
  


<div class="background-white">
    <div id="is24-footer" class="">
        
            
            
                <style>
	footer.page-footer .font-s.font-lightgray {
		color: #333333 !important;
		font-weight: bold;
	}

	footer.page-footer li a,
	footer.page-footer li a:link,
	footer.page-footer li a:visited,
	footer.page-footer li a:hover,
	footer.page-footer li a:active {
		color: #757575;
		padding-left: 0;
	}

	footer.page-footer li a::before,
	footer.page-footer li a:link::before,
	footer.page-footer li a:visited::before,
	footer.page-footer li a:hover::before,
	footer.page-footer li a:active::before {
		content: none;
  }

  @media (max-width: 1013px) {
    footer.page-footer li.inline-link {
      display: block;
    }
  }

  @media (min-width: 1014px) {
    footer.page-footer li.inline-link {
        display: inline-block;
    }

    footer.page-footer li.with-pipe--left {
        margin-left: 4px;
        padding-left: 4px;
        position: relative;
    }
    footer.page-footer li.with-pipe--left::before {
        content: '';
        position: absolute;
        display: block;
        height: 14px;
        width: 1px;
        background: #757575;
        top: 4px;
        left: 0;
    }
  }
</style>

<footer class="page-footer font-s" role="contentinfo" data-cms-qa="page-footer" data-path="default2023">
	<section class="content-wrapper">
    <div class="margin-top-xl margin-bottom-l">
			<div class="grid gutter">
				<div class="grid-item palm-one-half lap-one-fourth desk-one-fourth">
					<section>
						<div class="font-s font-line-s font-bold margin-bottom-s">Über ImmoScout24</div>
						<div class="list1 listexternal parbase"><ul class="icon-arrow list-spacing-xs">
    <li><a href="/unternehmen">Über uns</a></li>
    <li><a href="https://www.immobilienscout24.de/unternehmen/karriere">Karriere</a></li>
    <li><a href="/sitemap.html">Sitemap</a></li>
    <li><a href="/impressum.html">Impressum</a></li>
    </ul>
</div>
</section>
				</div>
        <div class="grid-item palm-one-half lap-one-fourth desk-one-fourth">
					<section>
						<div class="font-s font-line-s font-bold margin-bottom-s">Services</div>
						<div class="list2 listexternal parbase"><ul class="icon-arrow list-spacing-xs">
    <li><a href="/kontakt">Kontakt &amp; Hilfe</a></li>
    <li><a href="/unternehmen/mediendienst.html">Presseservice</a></li>
    <li><a href="/ratgeber/newsletter.html">Newsletter abonnieren</a></li>
    <li><a href="/anbieten/kuendigung.html">Verträge hier kündigen</a></li>
    <li><a href="https://api.immobilienscout24.de/">IT &amp; Entwicklung</a></li>
    <li><a href="https://atlas.immobilienscout24.de/">Preisatlas</a></li>
    <li><a href="https://www.immobilienscout24.at/">ImmoScout24 Österreich</a></li>
    </ul>
</div>
</section>
				</div>
        <div class="grid-item palm-one-half lap-one-fourth desk-one-fourth">
					<section>
						<div class="font-s font-line-s font-bold margin-bottom-s">Sicherheit</div>
						<div class="list3 listexternal parbase"><ul class="icon-arrow list-spacing-xs">
    <li><a href="/agb.html">AGB &amp; Rechtliche Hinweise</a></li>
    <li><a href="/agb/verbraucherinformationen.html">Verbraucherinformationen</a></li>
    <li class="inline-link"><a href="/agb/datenschutz.html">Datenschutz</a> | <a id="privacyManagerLink" href="javascript:;">Zum Privacy Manager</a></li>
    <li><a href="/lp/Geodatenkodex.html">Datenschutz-Kodex für Geodatendienste</a></li>
    <li><a href="https://sicherheit.immobilienscout24.de/">Sicherheit</a></li>
    </ul>
</div>
</section>
        </div>
        <div class="grid-item palm-one-half lap-one-fourth desk-one-fourth">
          <section>
            <div class="font-s font-line-s font-bold margin-bottom-s">Für Profis</div>
						<div class="list4 listexternal parbase"><ul class="icon-arrow list-spacing-xs">
    <li><a href="/anbieten/gewerbliche-anbieter.html">Produktwelten</a></li>
    <li><a href="https://www.immobilienscout24.de/anbieter/immobilienmakler">Maklernetzwerk</a></li>
    <li><a href="/immobilienmakler/lp/eigentuemer-leads-kaufen.html">Eigentümeranfragen</a></li>
    <li><a href="/baufinanzierung/produkte.html">Finanzierungsanfragen</a></li>
    <li><a href="/umzug/editionen.html">Umzugsanfragen</a></li>
    <li><a href="https://www.scout24media.com/" target="_blank" rel="nofollow">Werben mit uns</a></li>
    </ul>
</div>
<a href="https://www.immobilienscout24.de/lp/kunde-werden.html?cmp_id=10-04704&amp;cmp_name=default_customer_lp&amp;cmp_position=default_content&amp;cmp_creative=footer_cta" class="button margin-top-s">Kunde werden</a>
					</section>
				</div>
      </div>
      <div class="grid grid-flex gutter grid-justify-center">
        <div class="grid-item palm-one-whole">
          <div class="font-s font-line-s font-bold margin-bottom-s">App herunterladen</div>
          <div class="app-store-badges">
            <a href="https://app.adjust.com/10dzke3c?deep_link=is24%3A%2F%2FretargetHome&amp;redirect=https%3A%2F%2Fapps.apple.com%2Fde%2Fapp%2Fimmoscout24-immobilien%2Fid344176018&amp;redirect_macos=https%3A%2F%2Fapps.apple.com%2Fde%2Fapp%2Fimmoscout24-immobilien%2Fid344176018" title="ImmoScout24 im Apple App Store" target="_blank" rel="nofollow">
              <svg id="livetype" xmlns="http://www.w3.org/2000/svg" width="100" height="33" viewBox="0 0 119.66407 40">
                <g>
                  <g>
                    <g>
                      <path d="M110.13477,0H9.53468c-.3667,0-.729,0-1.09473.002-.30615.002-.60986.00781-.91895.0127A13.21476,13.21476,0,0,0,5.5171.19141a6.66509,6.66509,0,0,0-1.90088.627A6.43779,6.43779,0,0,0,1.99757,1.99707,6.25844,6.25844,0,0,0,.81935,3.61816a6.60119,6.60119,0,0,0-.625,1.90332,12.993,12.993,0,0,0-.1792,2.002C.00587,7.83008.00489,8.1377,0,8.44434V31.5586c.00489.3105.00587.6113.01515.9219a12.99232,12.99232,0,0,0,.1792,2.0019,6.58756,6.58756,0,0,0,.625,1.9043A6.20778,6.20778,0,0,0,1.99757,38.001a6.27445,6.27445,0,0,0,1.61865,1.1787,6.70082,6.70082,0,0,0,1.90088.6308,13.45514,13.45514,0,0,0,2.0039.1768c.30909.0068.6128.0107.91895.0107C8.80567,40,9.168,40,9.53468,40H110.13477c.3594,0,.7246,0,1.084-.002.3047,0,.6172-.0039.9219-.0107a13.279,13.279,0,0,0,2-.1768,6.80432,6.80432,0,0,0,1.9082-.6308,6.27742,6.27742,0,0,0,1.6172-1.1787,6.39482,6.39482,0,0,0,1.1816-1.6143,6.60413,6.60413,0,0,0,.6191-1.9043,13.50643,13.50643,0,0,0,.1856-2.0019c.0039-.3106.0039-.6114.0039-.9219.0078-.3633.0078-.7246.0078-1.0938V9.53613c0-.36621,0-.72949-.0078-1.09179,0-.30664,0-.61426-.0039-.9209a13.5071,13.5071,0,0,0-.1856-2.002,6.6177,6.6177,0,0,0-.6191-1.90332,6.46619,6.46619,0,0,0-2.7988-2.7998,6.76754,6.76754,0,0,0-1.9082-.627,13.04394,13.04394,0,0,0-2-.17676c-.3047-.00488-.6172-.01074-.9219-.01269-.3594-.002-.7246-.002-1.084-.002Z" style="fill: #a6a6a6"></path>
                      <path d="M8.44483,39.125c-.30468,0-.602-.0039-.90429-.0107a12.68714,12.68714,0,0,1-1.86914-.1631,5.88381,5.88381,0,0,1-1.65674-.5479,5.40573,5.40573,0,0,1-1.397-1.0166,5.32082,5.32082,0,0,1-1.02051-1.3965,5.72186,5.72186,0,0,1-.543-1.6572,12.41351,12.41351,0,0,1-.1665-1.875c-.00634-.2109-.01464-.9131-.01464-.9131V8.44434S.88185,7.75293.8877,7.5498a12.37039,12.37039,0,0,1,.16553-1.87207,5.7555,5.7555,0,0,1,.54346-1.6621A5.37349,5.37349,0,0,1,2.61183,2.61768,5.56543,5.56543,0,0,1,4.01417,1.59521a5.82309,5.82309,0,0,1,1.65332-.54394A12.58589,12.58589,0,0,1,7.543.88721L8.44532.875H111.21387l.9131.0127a12.38493,12.38493,0,0,1,1.8584.16259,5.93833,5.93833,0,0,1,1.6709.54785,5.59374,5.59374,0,0,1,2.415,2.41993,5.76267,5.76267,0,0,1,.5352,1.64892,12.995,12.995,0,0,1,.1738,1.88721c.0029.2832.0029.5874.0029.89014.0079.375.0079.73193.0079,1.09179V30.4648c0,.3633,0,.7178-.0079,1.0752,0,.3252,0,.6231-.0039.9297a12.73126,12.73126,0,0,1-.1709,1.8535,5.739,5.739,0,0,1-.54,1.67,5.48029,5.48029,0,0,1-1.0156,1.3857,5.4129,5.4129,0,0,1-1.3994,1.0225,5.86168,5.86168,0,0,1-1.668.5498,12.54218,12.54218,0,0,1-1.8692.1631c-.2929.0068-.5996.0107-.8974.0107l-1.084.002Z"></path>
                    </g>
                    <g id="_Group_" data-name="<Group>">
                      <g id="_Group_2" data-name="<Group>">
                        <g id="_Group_3" data-name="<Group>">
                          <path id="_Path_" data-name="<Path>" d="M24.76888,20.30068a4.94881,4.94881,0,0,1,2.35656-4.15206,5.06566,5.06566,0,0,0-3.99116-2.15768c-1.67924-.17626-3.30719,1.00483-4.1629,1.00483-.87227,0-2.18977-.98733-3.6085-.95814a5.31529,5.31529,0,0,0-4.47292,2.72787c-1.934,3.34842-.49141,8.26947,1.3612,10.97608.9269,1.32535,2.01018,2.8058,3.42763,2.7533,1.38706-.05753,1.9051-.88448,3.5794-.88448,1.65876,0,2.14479.88448,3.591.8511,1.48838-.02416,2.42613-1.33124,3.32051-2.66914a10.962,10.962,0,0,0,1.51842-3.09251A4.78205,4.78205,0,0,1,24.76888,20.30068Z" style="fill: #fff"></path>
                          <path id="_Path_2" data-name="<Path>" d="M22.03725,12.21089a4.87248,4.87248,0,0,0,1.11452-3.49062,4.95746,4.95746,0,0,0-3.20758,1.65961,4.63634,4.63634,0,0,0-1.14371,3.36139A4.09905,4.09905,0,0,0,22.03725,12.21089Z" style="fill: #fff"></path>
                        </g>
                      </g>
                      <g>
                        <path d="M42.30227,27.13965h-4.7334l-1.13672,3.35645H34.42727l4.4834-12.418h2.083l4.4834,12.418H43.438ZM38.0591,25.59082h3.752l-1.84961-5.44727h-.05176Z" style="fill: #fff"></path>
                        <path d="M55.15969,25.96973c0,2.81348-1.50586,4.62109-3.77832,4.62109a3.0693,3.0693,0,0,1-2.84863-1.584h-.043v4.48438h-1.8584V21.44238H48.4302v1.50586h.03418a3.21162,3.21162,0,0,1,2.88281-1.60059C53.645,21.34766,55.15969,23.16406,55.15969,25.96973Zm-1.91016,0c0-1.833-.94727-3.03809-2.39258-3.03809-1.41992,0-2.375,1.23047-2.375,3.03809,0,1.82422.95508,3.0459,2.375,3.0459C52.30227,29.01563,53.24953,27.81934,53.24953,25.96973Z" style="fill: #fff"></path>
                        <path d="M65.12453,25.96973c0,2.81348-1.50586,4.62109-3.77832,4.62109a3.0693,3.0693,0,0,1-2.84863-1.584h-.043v4.48438h-1.8584V21.44238H58.395v1.50586h.03418A3.21162,3.21162,0,0,1,61.312,21.34766C63.60988,21.34766,65.12453,23.16406,65.12453,25.96973Zm-1.91016,0c0-1.833-.94727-3.03809-2.39258-3.03809-1.41992,0-2.375,1.23047-2.375,3.03809,0,1.82422.95508,3.0459,2.375,3.0459C62.26711,29.01563,63.21438,27.81934,63.21438,25.96973Z" style="fill: #fff"></path>
                        <path d="M71.71047,27.03613c.1377,1.23145,1.334,2.04,2.96875,2.04,1.56641,0,2.69336-.80859,2.69336-1.91895,0-.96387-.67969-1.541-2.28906-1.93652l-1.60937-.3877c-2.28027-.55078-3.33887-1.61719-3.33887-3.34766,0-2.14258,1.86719-3.61426,4.51855-3.61426,2.624,0,4.42285,1.47168,4.4834,3.61426h-1.876c-.1123-1.23926-1.13672-1.9873-2.63379-1.9873s-2.52148.75684-2.52148,1.8584c0,.87793.6543,1.39453,2.25488,1.79l1.36816.33594c2.54785.60254,3.60645,1.626,3.60645,3.44238,0,2.32324-1.85059,3.77832-4.79395,3.77832-2.75391,0-4.61328-1.4209-4.7334-3.667Z" style="fill: #fff"></path>
                        <path d="M83.34621,19.2998v2.14258h1.72168v1.47168H83.34621v4.99121c0,.77539.34473,1.13672,1.10156,1.13672a5.80752,5.80752,0,0,0,.61133-.043v1.46289a5.10351,5.10351,0,0,1-1.03223.08594c-1.833,0-2.54785-.68848-2.54785-2.44434V22.91406H80.16262V21.44238H81.479V19.2998Z" style="fill: #fff"></path>
                        <path d="M86.065,25.96973c0-2.84863,1.67773-4.63867,4.29395-4.63867,2.625,0,4.29492,1.79,4.29492,4.63867,0,2.85645-1.66113,4.63867-4.29492,4.63867C87.72609,30.6084,86.065,28.82617,86.065,25.96973Zm6.69531,0c0-1.9541-.89551-3.10742-2.40137-3.10742s-2.40039,1.16211-2.40039,3.10742c0,1.96191.89453,3.10645,2.40039,3.10645S92.76027,27.93164,92.76027,25.96973Z" style="fill: #fff"></path>
                        <path d="M96.18606,21.44238h1.77246v1.541h.043a2.1594,2.1594,0,0,1,2.17773-1.63574,2.86616,2.86616,0,0,1,.63672.06934v1.73828a2.59794,2.59794,0,0,0-.835-.1123,1.87264,1.87264,0,0,0-1.93652,2.083v5.37012h-1.8584Z" style="fill: #fff"></path>
                        <path d="M109.3843,27.83691c-.25,1.64355-1.85059,2.77148-3.89844,2.77148-2.63379,0-4.26855-1.76465-4.26855-4.5957,0-2.83984,1.64355-4.68164,4.19043-4.68164,2.50488,0,4.08008,1.7207,4.08008,4.46582v.63672h-6.39453v.1123a2.358,2.358,0,0,0,2.43555,2.56445,2.04834,2.04834,0,0,0,2.09082-1.27344Zm-6.28223-2.70215h4.52637a2.1773,2.1773,0,0,0-2.2207-2.29785A2.292,2.292,0,0,0,103.10207,25.13477Z" style="fill: #fff"></path>
                      </g>
                    </g>
                  </g>
                  <g id="_Group_4" data-name="<Group>">
                    <g>
                      <path d="M39.3926,14.69775H35.67092V8.731h.92676V13.8457H39.3926Z" style="fill: #fff"></path>
                      <path d="M40.32912,13.42432c0-.81055.60352-1.27783,1.6748-1.34424l1.21973-.07031v-.38867c0-.47559-.31445-.74414-.92187-.74414-.49609,0-.83984.18213-.93848.50049h-.86035c.09082-.77344.81836-1.26953,1.83984-1.26953,1.12891,0,1.76563.562,1.76563,1.51318v3.07666h-.85547v-.63281h-.07031a1.515,1.515,0,0,1-1.35254.707A1.36026,1.36026,0,0,1,40.32912,13.42432Zm2.89453-.38477v-.37646L42.124,12.7334c-.62012.0415-.90137.25244-.90137.64941,0,.40527.35156.64111.835.64111A1.0615,1.0615,0,0,0,43.22365,13.03955Z" style="fill: #fff"></path>
                      <path d="M45.27639,12.44434c0-1.42285.73145-2.32422,1.86914-2.32422a1.484,1.484,0,0,1,1.38086.79h.06641V8.437h.88867v6.26074H48.6299v-.71143h-.07031a1.56284,1.56284,0,0,1-1.41406.78564C46,14.772,45.27639,13.87061,45.27639,12.44434Zm.918,0c0,.95508.4502,1.52979,1.20313,1.52979.749,0,1.21191-.583,1.21191-1.52588,0-.93848-.46777-1.52979-1.21191-1.52979C46.64943,10.91846,46.19436,11.49707,46.19436,12.44434Z" style="fill: #fff"></path>
                      <path d="M54.74709,13.48193a1.828,1.828,0,0,1-1.95117,1.30273,2.04531,2.04531,0,0,1-2.08008-2.32422A2.07685,2.07685,0,0,1,52.792,10.10791c1.25293,0,2.00879.856,2.00879,2.27V12.688H51.62111v.0498a1.1902,1.1902,0,0,0,1.19922,1.29,1.07934,1.07934,0,0,0,1.07129-.5459Zm-3.126-1.45117h2.27441a1.08647,1.08647,0,0,0-1.1084-1.1665A1.15162,1.15162,0,0,0,51.62111,12.03076Z" style="fill: #fff"></path>
                      <path d="M55.99416,10.19482h.85547v.71533H56.916a1.348,1.348,0,0,1,1.34375-.80225,1.46456,1.46456,0,0,1,1.55859,1.6748v2.915h-.88867V12.00586c0-.72363-.31445-1.0835-.97168-1.0835a1.03294,1.03294,0,0,0-1.0752,1.14111v2.63428h-.88867Z" style="fill: #fff"></path>
                      <path d="M63.51955,8.86328a.57572.57572,0,1,1,.5752.5415A.54735.54735,0,0,1,63.51955,8.86328Zm.13281,1.33154h.88477v4.50293h-.88477Z" style="fill: #fff"></path>
                      <path d="M65.97121,10.19482h.85547v.72363h.06641a1.36385,1.36385,0,0,1,2.49316,0h.07031a1.46325,1.46325,0,0,1,1.36914-.81055,1.33821,1.33821,0,0,1,1.43848,1.48828v3.10156h-.88867V11.82813c0-.60791-.29-.90576-.873-.90576a.91167.91167,0,0,0-.9502.94287v2.83252h-.873V11.74121a.78468.78468,0,0,0-.86816-.81885.96854.96854,0,0,0-.95117,1.02148v2.75391h-.88867Z" style="fill: #fff"></path>
                    </g>
                  </g>
                </g>
              </svg>
            </a>
            <a href="https://app.adjust.com/105sq3z6?deep_link=is24%3A%2F%2FretargetHome&amp;fallback=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dde.is24.android%26hl%3Dde%26gl%3Dde&amp;redirect_macos=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dde.is24.android%26hl%3Dde%26gl%3DUS" title="ImmoScout24 im Google Play Store" target="_blank" rel="nofollow">
              <img src="https://www.static-immobilienscout24.de/fro/footer/logos/google_play.png" alt="Google Play Store Logo" width="110" loading="lazy">
            </a>
          </div>
        </div>
        <div class="grid-item palm-one-whole">
          <div class="font-s font-line-s font-bold margin-bottom-s">Folge uns</div>
          <a href="https://www.facebook.com/ImmoScout24" class="margin-right-s" title="ImmoScout24 auf Facebook" aria-label="ImmoScout24 auf Facebook" target="_blank" rel="nofollow">
            <svg width="32" height="32" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M24 4C12.954 4 4 12.954 4 24C4 33.982 11.314 42.256 20.876 43.758V29.78H15.796V24H20.876V19.594C20.876 14.582 23.86 11.814 28.43 11.814C30.618 11.814 32.906 12.204 32.906 12.204V17.124H30.386C27.9 17.124 27.126 18.666 27.126 20.248V24H32.672L31.786 29.78H27.126V43.758C36.686 42.258 44 33.98 44 24C44 12.954 35.046 4 24 4Z" fill="#1877F2"></path>
</svg>
</a>
          <a href="https://www.instagram.com/immobilienscout24" class="margin-right-s" title="ImmoScout24 auf Instagram" aria-label="ImmoScout24 auf Instagram" target="_blank" rel="nofollow">
            <svg style="enable-background:new 0 0 512 512;" version="1.1" width="32" height="32" viewBox="0 0 512 512" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <style type="text/css">
	.st0{fill:url(#SVGID_1_);}
	.st1{fill:url(#SVGID_2_);}
	.st2{fill:#654C9F;}
  </style>
  <g id="Edges"></g><g id="Symbol"><g><radialGradient cx="56.3501" cy="19.2179" gradientTransform="matrix(0.9986 -5.233596e-02 4.448556e-02 0.8488 -36.9742 443.8014)" gradientUnits="userSpaceOnUse" id="SVGID_1_" r="711.335"><stop offset="0" style="stop-color:#FED576"></stop><stop offset="0.2634" style="stop-color:#F47133"></stop><stop offset="0.6091" style="stop-color:#BC3081"></stop><stop offset="1" style="stop-color:#4C63D2"></stop></radialGradient><path class="st0" d="M96.1,23.2c-16.2,6.3-29.9,14.7-43.6,28.4C38.8,65.2,30.4,79,24.1,95.1c-6.1,15.6-10.2,33.5-11.4,59.7    c-1.2,26.2-1.5,34.6-1.5,101.4s0.3,75.2,1.5,101.4c1.2,26.2,5.4,44.1,11.4,59.7c6.3,16.2,14.7,29.9,28.4,43.6    c13.7,13.7,27.4,22.1,43.6,28.4c15.6,6.1,33.5,10.2,59.7,11.4c26.2,1.2,34.6,1.5,101.4,1.5c66.8,0,75.2-0.3,101.4-1.5    c26.2-1.2,44.1-5.4,59.7-11.4c16.2-6.3,29.9-14.7,43.6-28.4c13.7-13.7,22.1-27.4,28.4-43.6c6.1-15.6,10.2-33.5,11.4-59.7    c1.2-26.2,1.5-34.6,1.5-101.4s-0.3-75.2-1.5-101.4c-1.2-26.2-5.4-44.1-11.4-59.7C484,79,475.6,65.2,462,51.6    c-13.7-13.7-27.4-22.1-43.6-28.4c-15.6-6.1-33.5-10.2-59.7-11.4c-26.2-1.2-34.6-1.5-101.4-1.5s-75.2,0.3-101.4,1.5    C129.6,12.9,111.7,17.1,96.1,23.2z M356.6,56c24,1.1,37,5.1,45.7,8.5c11.5,4.5,19.7,9.8,28.3,18.4c8.6,8.6,13.9,16.8,18.4,28.3    c3.4,8.7,7.4,21.7,8.5,45.7c1.2,25.9,1.4,33.7,1.4,99.4s-0.3,73.5-1.4,99.4c-1.1,24-5.1,37-8.5,45.7c-4.5,11.5-9.8,19.7-18.4,28.3    c-8.6,8.6-16.8,13.9-28.3,18.4c-8.7,3.4-21.7,7.4-45.7,8.5c-25.9,1.2-33.7,1.4-99.4,1.4s-73.5-0.3-99.4-1.4    c-24-1.1-37-5.1-45.7-8.5c-11.5-4.5-19.7-9.8-28.3-18.4c-8.6-8.6-13.9-16.8-18.4-28.3c-3.4-8.7-7.4-21.7-8.5-45.7    c-1.2-25.9-1.4-33.7-1.4-99.4s0.3-73.5,1.4-99.4c1.1-24,5.1-37,8.5-45.7c4.5-11.5,9.8-19.7,18.4-28.3c8.6-8.6,16.8-13.9,28.3-18.4    c8.7-3.4,21.7-7.4,45.7-8.5c25.9-1.2,33.7-1.4,99.4-1.4S330.7,54.8,356.6,56z"></path><radialGradient cx="154.0732" cy="134.5501" gradientTransform="matrix(0.9986 -5.233596e-02 4.448556e-02 0.8488 -24.3617 253.2946)" gradientUnits="userSpaceOnUse" id="SVGID_2_" r="365.2801"><stop offset="0" style="stop-color:#FED576"></stop><stop offset="0.2634" style="stop-color:#F47133"></stop><stop offset="0.6091" style="stop-color:#BC3081"></stop><stop offset="1" style="stop-color:#4C63D2"></stop></radialGradient><path class="st1" d="M130.9,256.3c0,69.8,56.6,126.3,126.3,126.3s126.3-56.6,126.3-126.3S327,130,257.2,130    S130.9,186.5,130.9,256.3z M339.2,256.3c0,45.3-36.7,82-82,82s-82-36.7-82-82c0-45.3,36.7-82,82-82S339.2,211,339.2,256.3z"></path><circle class="st2" cx="388.6" cy="125" r="29.5"></circle></g></g>
</svg>
</a>
          <a href="https://www.youtube.com/@ImmoScout24" class="margin-right-s" title="ImmoScout24 auf YouTube" aria-label="ImmoScout24 auf YouTube" target="_blank" rel="nofollow">
            <svg width="32" height="32" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M43.086 12.996C44 16.56 44 24 44 24C44 24 44 31.44 43.086 35.004C42.578 36.974 41.092 38.524 39.21 39.048C35.792 40 24 40 24 40C24 40 12.214 40 8.79 39.048C6.9 38.516 5.416 36.968 4.914 35.004C4 31.44 4 24 4 24C4 24 4 16.56 4.914 12.996C5.422 11.026 6.908 9.476 8.79 8.952C12.214 8 24 8 24 8C24 8 35.792 8 39.21 8.952C41.1 9.484 42.584 11.032 43.086 12.996ZM20 31L32 24L20 17V31Z" fill="#FF0000"></path>
</svg>
</a>
          <a href="https://www.tiktok.com/@immoscout24" class="margin-right-s" title="ImmoScout24 auf Tiktok" aria-label="ImmoScout24 auf Tiktok" target="_blank" rel="nofollow">
            <svg width="32" height="32" viewBox="-58.35000000000002 -186.70564362582354 2548.289756960746 2538.849821747569" xmlns="http://www.w3.org/2000/svg"><g fill="#25f4ee"><path d="M779.38 890.55v-88.12a650.81 650.81 0 0 0-92.45-7.94c-299.8-.64-565.22 193.64-655.25 479.6S47.92 1871.34 294 2042.56a684.7 684.7 0 0 1 485.36-1152z"></path><path d="M796 1888.72c167.62-.23 305.4-132.28 312.74-299.74V94.62h273A512.17 512.17 0 0 1 1373.8 0h-373.41v1492.92c-6.21 168.31-144.32 301.63-312.74 301.9a317.76 317.76 0 0 1-144.45-36.11A313.48 313.48 0 0 0 796 1888.72zM1891.66 601.64v-83.06a509.85 509.85 0 0 1-282.4-85.22 517.79 517.79 0 0 0 282.4 168.28z"></path></g><path d="M1609.26 433.36a514.19 514.19 0 0 1-127.84-339.47h-99.68a517.16 517.16 0 0 0 227.52 339.47zM686.93 1167.9a313.46 313.46 0 0 0-144.46 590.81A312.75 312.75 0 0 1 796 1262.51a329.69 329.69 0 0 1 92.44 14.49V897.05a654.77 654.77 0 0 0-92.44-7.22h-16.62v288.9a321.13 321.13 0 0 0-92.45-10.83z" fill="#fe2c55"></path><path d="M1891.66 601.64v288.91a886.23 886.23 0 0 1-517.86-168.29v759.1c-.8 378.78-308.09 685.43-686.87 685.43A679.65 679.65 0 0 1 294 2042.56 685.43 685.43 0 0 0 1481.42 1576V819.05A887.71 887.71 0 0 0 2000 985.17v-372a529.59 529.59 0 0 1-108.34-11.53z" fill="#fe2c55"></path><path d="M1373.8 1481.36v-759.1a886.11 886.11 0 0 0 518.58 166.12v-288.9a517.87 517.87 0 0 1-283.12-166.12 517.16 517.16 0 0 1-227.52-339.47h-273V1589a313.46 313.46 0 0 1-567 171.17 313.46 313.46 0 0 1 144.46-590.83 321.35 321.35 0 0 1 92.45 14.45V894.88A684.71 684.71 0 0 0 293.29 2050.5a679.65 679.65 0 0 0 393.64 116.29c378.78 0 686.07-306.65 686.87-685.43z"></path></svg>
</a>
          <a href="https://www.linkedin.com/company/immoscout24" title="ImmoScout24 auf LinkedIn" aria-label="ImmoScout24 auf LinkedIn" target="_blank" rel="nofollow">
            <svg width="32" height="32" viewBox="0 0 32 32">
  <path fill="#0b66c2" d="M24.447 24.452h-3.553v-5.569c0-1.328-0.027-3.037-1.853-3.037-1.852 0-2.135 1.445-2.135 2.94v5.667h-3.555v-11.452h3.413v1.56h0.047c0.477-0.899 1.637-1.849 3.371-1.849 3.6 0 4.267 2.371 4.267 5.455v6.287h-0.001zM9.337 11.433c-0.548 0.001-1.073-0.217-1.461-0.604s-0.604-0.913-0.603-1.461c0.001-1.14 0.925-2.063 2.065-2.063s2.063 0.925 2.063 2.065c-0.001 1.14-0.925 2.063-2.065 2.063h0.001zM11.119 24.452h-3.564v-11.452h3.565v11.452h-0.001zM26.227 4h-20.455c-0.981 0-1.772 0.773-1.772 1.729v20.541c0 0.956 0.792 1.729 1.771 1.729h20.451c0.979 0 1.779-0.773 1.779-1.729v-20.541c0-0.956-0.8-1.729-1.779-1.729h0.005z"></path>
</svg>
</a>
        </div>
      </div>
    </div>
    <div class="margin-bottom-l">
      <div class="grid grid-flex gutter-horizontal-m grid-justify-center grid-align-center" data-cms-qa="is24-cms-footer">
        <div class="grid-item">
          <a href="https://www.immobilienscout24.de/" class="grid-flex grid-align-center" title="ImmoScout24 - Die Nr. 1 für Immobilien" aria-label="ImmoScout24 - Die Nr. 1 für Immobilien"><img src="https://www.ImmoScout24.de/etc/designs/is24/img/immoscout24.svg" width="112" alt="ImmoScout24-Logo" loading="lazy">
          </a></div>
        <div class="grid-item font-s scout-claim ">
          Die Nr. 1 für Immobilien</div>
      </div>
		</div>
	</section>
  <div class="font-center">
    <div class="padding-vertical-l background-white">
      <div class="content-wrapper" data-cms-qa="is24-cms-footer-copyright">
        <span class="padding-right-s">© Copyright 2023</span><span class="immoscout-company-name">Immobilien Scout GmbH</span>
      </div>
		</div>
	</div>
</footer>

<script type="text/javascript">
  var datenschutzLinkNodeList = document.querySelectorAll('footer li a');
  var datenschutzLinkArr = Array.prototype.slice.call(datenschutzLinkNodeList);
  var datenschutzLinkEl = datenschutzLinkArr.filter(function(e) {
    return e.innerText.match(/^Datenschutz$/);
  })[0];
  if (datenschutzLinkEl) {
    var datenschutzLinkParent = datenschutzLinkEl.parentElement || null;
    var newListItem = document.createElement('li');
    newListItem.classList.add('inline-link', 'with-pipe--left');
    var privacyManagerLink = document.createElement('a');
    privacyManagerLink.innerText = 'Zum Privacy Manager';
    privacyManagerLink.id = 'footerPrivacyManager';
    privacyManagerLink.setAttribute('href', 'javascript:void(0)');
    datenschutzLinkParent.classList.add('inline-link');
    newListItem.appendChild(privacyManagerLink);
    datenschutzLinkEl.parentNode.insertAdjacentHTML('afterend', newListItem.outerHTML);
    document.addEventListener('click', function(e) {
      if(e.target && e.target.id === 'footerPrivacyManager'){
        e.preventDefault();
        (function safeCall() {
          if(!window.__tcfapi) {
            document.body.style.cursor = 'progress'
            setTimeout(safeCall, 500)
            return
          }
          if(document.body.style.cursor === 'progress') {
            document.body.style.cursor = 'default'
          }
          window.__tcfapi('showConsentManager', true);
        })()
      }
    });
  }
</script>

            
        
        




<div id="is24-build" class="padding-vertical-m padding-horizontal-none font-xs font-lightgray align-center">
  <p>pro-sea-bc7cb447f-j8whp - v7279</p>
</div>

        
    </div>
</div>

</div>

  </div>

  

  <script>
    window.IS24 = window.IS24 || {};
    IS24.ssoAppName = "search";
    IS24.applicationContext = "/Suche/error-reporter";
    IS24.ab = {};
    IS24.feature = {"PRICE_INSIGHTS_COLOR_SCHEME_PASTEL":true,
"DEBUG_OVERLAPPING":false,
"LAZY_LOAD_PROGRESSIVE":true,
"DISABLE_ADS":false,
"PRICE_DISTRIBUTION":false,
"NHB_IMAGE_BOOST":true,
"DISABLE_COMMERCIAL_REDIRECT":false,
"PRICE_INSIGHTS_SHOW_BUILDING_DETAILS":true,
"QA_ARE_FEATURE_SWITCHES_HEALTHY":false,
"MAP_LIVE":false,
"PRICE_INSIGHTS_WHITE_OUTLINES":true,
"ATTRIBUTE_SEARCH":false,
"PROJECT_BOOST_SORTING":true,
"HIDE_DISTANCE_FOR_HIDDEN_ADDRESSES":true,
"RECO_RANDOM":false,
"DISABLE_TEALIUM":false,
"WEBP_SUPPORT":true,
"SORTING_INFO":true,
"SHOW_SUSTAINABILITY_BADGE":false,
"COLLECT_WEB_VITALS":true,
"RECO_FOR_ALL_REAL_ESTATE_TYPES":false,
"PRICE_INSIGHTS_USE_TOUCHPOINT":false,
"REPORT_TO_GDPR_DATA_LAKE":true,
"LOCAL_HERO":true,
"SERVER_SIDE_RENDERING_DISABLED":false,
"SEO_THUERINGEN":true,
"PRICE_INSIGHTS_COLOR_SCHEME_DYNAMIC":true,
"PURE_COCKPIT":false,
"PRICE_INSIGHTS_CLICKABLE_BUILDING_SHAPES":true,
"DISABLE_SAVED_SEARCH_FOR_AT_SUBREGIONS":false,
"HIDE_DISTANCE_FOR_HIDDEN_ADDRESSES_IN_API":false,
"REQUIRE_VALID_NONCE_TOKEN":false,
"LISTING_XXL":false,
"DEV_MODE":false,
"SHOW_CMS_HEADER_FOOTER":false,
"ENABLE_FLOODED_GROUPING":false,
"TOTAL_RENT":true,
"TRACKING_VERIFICATION":false,
"SCRAPER_DETECTION_LOGGING":false,
"SCHEMA_ORG_MARKUP":true,
"LIST_ONLY_IS24":true,
"USE_PDEV_RENT":true,
"FAIR_PRICE":false,
"OTP_PERFORMANCE_RESULT_LIST_REPORTING":true,
"SCRAPER_DETECTION_JS":true,
"PAGE_SPEED":false,
"ENABLE_BRANCH_BANNER":true,
"EXCLUDE_SWAP_FLATS":false,
"USE_TOUCHPOINTS":true,
"USE_TOUCHPOINTS_RENT":true,
"SHOW_BIG_MAP":false,
"SPECIAL_EVENT_MAP_ICONS":false,
"REPORT_TO_FIREHOSE":true,
"X_TYPE_SEARCH":false,
"DUMP_SSR_TIMEOUT_DATA":false,
"OBFUSCATE_HIDDEN_LOCATION":true,
"PRICE_TAB_NEW_LABEL":false};
    IS24.resultList = {
      gacApiKey: "49f5bf376feed3a0f0a52abb46c0dc90",
      gacBaseUrl: "",
      gacCountry: "DEU",
      navigationBarUrl: "/Suche/radius/wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0",
      searchUrl: "/radius/wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0",
      searchId: "e9ba9473-0b55-3f8a-a5b0-6b676b425d2e",
      isMobile: false,
      resultListModel: {"searchResponseModel":{"additional":{"lastSearchApiUrl":"/radius?realestatetype=apartmentrent&centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pagesize=20&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0&pagenumber=1","title":"Wohnung mieten im Umkreis von 5 km von Gießen (Kreis) - ImmoScout24","sortingOptions":[{"description":"Standardsortierung","code":0},{"description":"Kaltmiete (höchste zuerst)","code":3},{"description":"Kaltmiete (niedrigste zuerst)","code":4},{"description":"Entfernung (niedrigste zuerst)","code":1},{"description":"Zimmeranzahl (höchste zuerst)","code":5},{"description":"Zimmeranzahl (niedrigste zuerst)","code":6},{"description":"Wohnfläche (größte zuerst)","code":7},{"description":"Wohnfläche (kleinste zuerst)","code":8},{"description":"Aktualität (neueste zuerst)","code":2}],"pagerTemplate":"|Suche|radius|wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0&pagenumber=%page%","sortingTemplate":"|Suche|radius|wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0&sorting=%sorting%","world":"LIVING","international":false,"device":{"desktop":true},"commercial":false,"saveSearchLink":"/Suche/controller/saveSearch.go?reportLabelSaveSearchLocation=textlink&searchUrl=/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&returnUrl=/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&source=savedsearch","saveSearchBottomLink":"/Suche/controller/saveSearch.go?reportLabelSaveSearchLocation=button&searchUrl=/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&returnUrl=/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&source=savedsearch","saveSearchSidebarLink":"/Suche/controller/saveSearch.go?reportLabelSaveSearchLocation=contentbox&searchUrl=/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&returnUrl=/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&source=savedsearch","saveSearchIcon":"/Suche/controller/saveSearch.go?reportLabelSaveSearchLocation=icon&searchUrl=/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&returnUrl=/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&source=savedsearch","propertyBookLinks":{"url":"https://atlas.immobilienscout24.de/hierarchy-page-by-id/1276007006005?marketingFocus=APARTMENT_RENT&cmp_id=10-04309&cmp_name=residential_atlas&cmp_position=residential_resultlist&cmp_creative=top_right_info_box_textlink_APARTMENT_RENT#/preis-%C3%BCbersicht","locationName":"Gießen","realEstateTypeToPriceHistoryWithTrend":{"APARTMENT_RENT":{"priceHistory":{"averagePrice":9.59,"forecast":{"percentageChange":1.04,"current":{"year":2023,"quarter":4},"next":{"year":2024,"quarter":1}}},"trend":"UP"}}},"resultlistShortDescription":"Mietwohnungen im Umkreis von 5 km von Gießen (Kreis)","saveable":true,"landingPageLayout":false,"regionCmsContentUrl":"/content/is24resultlist/radius/wohnung-mieten/_jcr_content/info.html","faqCmsContentUrl":"/content/is24resultlist/radius/wohnung-mieten/_jcr_content/faq.html","introCmsContentUrl":"/content/is24resultlist/radius/wohnung-mieten/_jcr_content/intro.html","seoLinks":null,"showProvisionsfrei":false,"footerData":"pro-sea-bc7cb447f-j8whp - v7279","realEstateTypes":["APARTMENT_RENT"],"realEstateTypesForMap":["FLAT_SHARE_ROOM","LIVING_RENT_SITE","SENIOR_CARE","ASSISTED_LIVING","INVESTMENT","LIVING_BUY_SITE","SHORT_TERM_ACCOMMODATION","GARAGE_BUY","GARAGE_RENT","APARTMENT_RENT","HOUSE_RENT","HOUSE_BUY","APARTMENT_BUY","COMPULSORY_AUCTION"],"map":{"shapeServerUrl":"https://geoservices.immobilienscout24.de","objectTilesVersion":"3","objectSearchBaseUrl":"https://www.search.immobilienscout24.de/Suche/controller/objectSearch","valuationShapeServiceUrl":"https://www.immobilienscout24.de/price-shape","priceShapeServiceUrl":"https://pro-is24-price-shape-service.is24-val.eu-west-1.infinity.s24cloud.net","googleMapsPriceAtlasMapId":"db17ef3b9009126a","objectSearchEnabled":true},"resultListQueryUrlTemplate":"/Suche/controller/mapResults.go?searchUrl=/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&pageSize=%pageSize%","messages":[],"version":"7279","queryModel":"{\"query\":{\"view\":\"IS24\",\"radius\":5.0,\"minRadius\":null,\"realEstateTypes\":[\"APARTMENT_RENT\"],\"realEstateType\":\"APARTMENT_RENT\",\"furnishing\":null,\"flatShareSize\":null,\"shortTermAccommodationType\":null,\"centerOfSearchAddress\":{\"geoCodeId\":1276007006005,\"region\":null,\"city\":\"Gießen (Kreis)\",\"quarter\":\"Gießen\",\"postcode\":null,\"street\":null,\"houseNumber\":null,\"cityPlusQuarter\":\"Gießen (Kreis)-Gießen\"},\"locationSelectionType\":\"VICINITY\",\"smokingAllowed\":null,\"flatMateGender\":null,\"assistedLivingCommercializationType\":null,\"apiField1\":null,\"apiField2\":null,\"apiField3\":null,\"fullTextQuery\":null,\"companyWideCustomerId\":null,\"numberOfPersons\":null,\"ownFunds\":null,\"vendorGroup\":null,\"minimumInternetSpeed\":null,\"beginRent\":null,\"rentalPeriod\":null,\"lastModifiedAfter\":null,\"rentDurationInMonths\":null,\"wohnberechtigungsscheinNeeded\":null,\"hasRented\":null,\"trailLivingPossible\":null,\"withFurniture\":null,\"smokingPermitted\":null,\"handoverPermitted\":null,\"liveVideoTourAvailable\":null,\"firstActivationRange\":null,\"priceRangeWithType\":{\"type\":\"RENT_PER_TIME\",\"range\":{\"min\":null,\"max\":800.0}},\"virtualTourType\":null,\"yearOfConstructionRange\":null,\"numberOfParkingSpacesRange\":null,\"numberOfSeatsRange\":null,\"numberOfBedsRange\":null,\"floorRange\":null,\"priceMultiplierRange\":null,\"netAreaRange\":null,\"numberOfRoomsRange\":{\"min\":2.0,\"max\":null},\"netRentRange\":null,\"lotSizeRange\":null,\"totalAreaRange\":null,\"siteAreaRange\":null,\"pricePerSqm\":null,\"priceRange\":null,\"totalRentRange\":null,\"marketValueRange\":null,\"monthlyRateRange\":null,\"onlyShortTermBuildable\":false,\"onlyBuildingProject\":false,\"onlyNewBuildingOrBuildingProject\":false,\"onlyWithBalcony\":false,\"onlyWithInternet\":false,\"onlyWithGarden\":false,\"onlyWithElevator\":false,\"onlyWithParking\":false,\"onlyWithBarrierFree\":false,\"onlyWithGuestToilet\":false,\"onlyWithBasement\":false,\"onlyWithLodgerFlat\":false,\"onlyWithAvailableHighVoltageCurrent\":false,\"onlyWithAmbulantNursingService\":false,\"onlySecondAuctions\":false,\"onlySplittingAuctions\":false,\"onlyWithCareOfAlzheimerDiseasePatients\":false,\"onlyWithCareOfArtificalRespirationPatients\":false,\"onlyWithCareOfDementiaPatients\":false,\"onlyWithCareOfMultipleSclerosisPatients\":false,\"onlyWithCareOfParkinsonsDiseasePatients\":false,\"onlyWithCareOfStrokePatients\":false,\"onlyWithCareOfVegetativeStatePatients\":false,\"onlyWithCooker\":false,\"onlyWithCookingPossibility\":false,\"onlyWithCraneRails\":false,\"onlyWithDishWasher\":false,\"onlyWithFridge\":false,\"onlyWithHoist\":false,\"onlyWithLiftingPlatform\":false,\"onlyWithOven\":false,\"onlyWithOwnFurnishingPossible\":false,\"onlyWithRamp\":false,\"onlyWithWashingMachine\":false,\"onlyWithoutCourtage\":false,\"onlyWithAirConditioning\":false,\"onlyWithItInfrastructure\":false,\"onlyWithKitchen\":false,\"onlyWithPlanningPermission\":false,\"onlyFlatShareSuitable\":false,\"onlyWithShowcaseOrPremium\":false,\"onlyNewHomeBuilder\":false,\"realEstateIds\":[],\"neighbourhoodIds\":[],\"shapeInformations\":[\"065310050600\"],\"apartmentTypes\":[],\"houseTypes\":[],\"houseTypeTypes\":[],\"officeTypes\":[],\"tradeSiteUtilizations\":[],\"gastronomyTypes\":[],\"storeTypes\":[],\"specialPurposePropertyTypes\":[],\"investObjectTypes\":[],\"industryTypes\":[],\"garageTypes\":[],\"careTypes\":[],\"auctionObjectTypes\":[],\"siteDevelopmentTypes\":[],\"siteConstructibleTypes\":[],\"constructionPhaseTypes\":[],\"seniorCareLevels\":[],\"roomTypes\":[],\"heatingTypes\":[],\"locationClassifications\":[],\"officeRentDurations\":[],\"energyEfficiencyClasses\":[],\"petsAllowedTypes\":[],\"exclusionCriteria\":[],\"verifiedBy\":[],\"listingTypes\":[],\"buildingProjectId\":null,\"shape\":null,\"clipShape\":null,\"centerOfSearchWgs84Coordinate\":{\"latitude\":50.58383,\"longitude\":8.67789},\"crossTypeSearch\":false,\"shapeSearch\":false,\"vicinitySearch\":true,\"geoHierarchySearch\":false,\"premiumDeveloperProject\":false},\"nonQueryData\":{\"locationName\":\"Gießen (Kreis)-Gießen\",\"gacLevel\":\"city\",\"otpEnabled\":true,\"sortingOption\":{\"description\":\"Standardsortierung\",\"code\":0},\"shapes\":null,\"geoPaths\":{\"065310050600\":\"/de/hessen/giessen-kreis/giessen/innenstadt\"},\"criteria\":[\"Mietwohnungen\",\"Gießen\",\"Umkreis 5 km\",\"ab 2 Zimmer\",\"bis 800 € Kaltmiete\"],\"international\":false,\"commercial\":false,\"rerenderAutocompleteField\":false},\"attributeSearchData\":{\"userText\":null,\"userHints\":null,\"uuId\":null}}","viewMode":"LIST","adsData":{"obj_regio1":"Hessen","obj_yearConstructedRange":"1,2,3,4,5,6,7,8,9","obj_noRoomsRange":"2,3,4,5","obj_ityp":"0","geo_land":"Deutschland","obj_baseRentRange":"1,2,3,4,5,6,7,8,9","obj_regio4":"Innenstadt","obj_regio3":"Gießen","obj_livingSpaceRange":"1,2,3,4,5,6,7,8,9,10","obj_regio2":"Gießen_Kreis","obj_radius":"5.0"},"featureSwitches":{"PRICE_INSIGHTS_COLOR_SCHEME_PASTEL":true,"DEBUG_OVERLAPPING":false,"LAZY_LOAD_PROGRESSIVE":true,"DISABLE_ADS":false,"PRICE_DISTRIBUTION":false,"NHB_IMAGE_BOOST":true,"DISABLE_COMMERCIAL_REDIRECT":false,"PRICE_INSIGHTS_SHOW_BUILDING_DETAILS":true,"QA_ARE_FEATURE_SWITCHES_HEALTHY":false,"MAP_LIVE":false,"PRICE_INSIGHTS_WHITE_OUTLINES":true,"ATTRIBUTE_SEARCH":false,"PROJECT_BOOST_SORTING":true,"HIDE_DISTANCE_FOR_HIDDEN_ADDRESSES":true,"RECO_RANDOM":false,"DISABLE_TEALIUM":false,"WEBP_SUPPORT":true,"SORTING_INFO":true,"SHOW_SUSTAINABILITY_BADGE":false,"COLLECT_WEB_VITALS":true,"RECO_FOR_ALL_REAL_ESTATE_TYPES":false,"PRICE_INSIGHTS_USE_TOUCHPOINT":false,"REPORT_TO_GDPR_DATA_LAKE":true,"LOCAL_HERO":true,"SERVER_SIDE_RENDERING_DISABLED":false,"SEO_THUERINGEN":true,"PRICE_INSIGHTS_COLOR_SCHEME_DYNAMIC":true,"PURE_COCKPIT":false,"PRICE_INSIGHTS_CLICKABLE_BUILDING_SHAPES":true,"DISABLE_SAVED_SEARCH_FOR_AT_SUBREGIONS":false,"HIDE_DISTANCE_FOR_HIDDEN_ADDRESSES_IN_API":false,"REQUIRE_VALID_NONCE_TOKEN":false,"LISTING_XXL":false,"DEV_MODE":false,"SHOW_CMS_HEADER_FOOTER":false,"ENABLE_FLOODED_GROUPING":false,"TOTAL_RENT":true,"TRACKING_VERIFICATION":false,"SCRAPER_DETECTION_LOGGING":false,"SCHEMA_ORG_MARKUP":true,"LIST_ONLY_IS24":true,"USE_PDEV_RENT":true,"FAIR_PRICE":false,"OTP_PERFORMANCE_RESULT_LIST_REPORTING":true,"SCRAPER_DETECTION_JS":true,"PAGE_SPEED":false,"ENABLE_BRANCH_BANNER":true,"EXCLUDE_SWAP_FLATS":false,"USE_TOUCHPOINTS":true,"USE_TOUCHPOINTS_RENT":true,"SHOW_BIG_MAP":false,"SPECIAL_EVENT_MAP_ICONS":false,"REPORT_TO_FIREHOSE":true,"X_TYPE_SEARCH":false,"DUMP_SSR_TIMEOUT_DATA":false,"OBFUSCATE_HIDDEN_LOCATION":true,"PRICE_TAB_NEW_LABEL":false},"abTestSwitches":{},"searchUrl":"/radius/wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0","counterName":"is24.de.finden.wohnen.wohnung_miete.result","seoHeaderBean":{"indexByRobots":false,"canonicalUrl":null,"description":"Ein großes Angebot an Mietwohnungen im Umkreis von 5 km von Gießen (Kreis) finden Sie bei ImmoScout24. Jetzt Ihre Traum-Wohnung im Umkreis von 5 km von Gießen (Kreis) mieten.","keywords":""},"utagData":{"KVrooms":"2.0","query_regio2":"gießen_kreis","query_regio1":"hessen","query_numberOfRoomsMin":"2.0","query_numberOfRoomsAvg":"2.0","ga_cd_cxp_referrer":"ONE_STEP_SEARCH","geo_ot":"innenstadt","query_regio4":"innenstadt","query_regio3":"gießen","obj_ityp":"Wohnung_Miete","geo_land":"deutschland","KVimmotype":"APARTMENT_RENT","timestamp":"11.2023","query_radius":"5.0","query_realEstateType":"APARTMENT_RENT","obj_resultlist_count":"21","obj_crosstype":"liv_apartment_rent","geo_bln":"hessen","KVcourtage":"y","geo_bg":"gießen","query_courtage":"y","ga_cd_cxp_resultview":"listview","query_timestamp":"11.2023","KVregio1":"hessen","geo_krs":"gießen_kreis"},"resultListUrl":"/Suche/radius/wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0","shapeSearchMode":"DRAWN","touchpointData":{"searchType":"radius","locationName":null,"geoIds":["065310050600"],"lng":8.67789,"lat":50.58383,"radius":5.0},"googleMapsApiKey":"AIzaSyDdzQFBEs4I22FSJmzDgCtSXWMipwqPEBQ","googleMapsApiVersion":"3.53","loggedIn":false,"interlinkingLists":null,"breadcrumbBean":{"links":[{"label":"Suche","url":"/"},{"label":"Hessen","url":"/Suche/de/hessen/wohnung-mieten"},{"label":"Gießen (Kreis)","url":"/Suche/de/hessen/giessen-kreis/wohnung-mieten"},{"label":"Gießen","url":"/Suche/de/hessen/giessen-kreis/giessen/wohnung-mieten"},{"label":"Innenstadt","url":"/Suche/de/hessen/giessen-kreis/giessen/innenstadt/wohnung-mieten"}]},"classicGeoCodes":"1276007006005","gacCountry":"DEU","gacSupported":true,"externalLinks":{"mieterPlusBookingUrl":"/warenkorb/mieterplus/?returnUrl=https://www.immobilienscout24.de/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0%26enteredFrom%3DBUY_MPLUS&cmp_id=10-051673&cmp_name=residential_profile&cmp_position=residential_resultlist&cmp_creative=modal_pawyall_cta","kaeuferPlusBookingUrl":"/warenkorb/kaeuferplus/?returnUrl=https://www.immobilienscout24.de/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0%26enteredFrom%3DBUY_KPLUS&cmp_id=10-051674&cmp_name=profile_buy_quickcheckout&cmp_position=residential_resultlist&cmp_creative=modal_paywall_cta","priceTabKaeuferPlusBookingUrl":"/warenkorb/kaeuferplus/?returnUrl=https://www.immobilienscout24.de/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0%26enteredFrom%3DBUY_KPLUS&cmp_id=10-051794&cmp_name=profile_buy_quickcheckout&cmp_position=residential_resultlist&cmp_creative=pricetrend_icon","atlasBaseUrl":"https://atlas.immobilienscout24.de","paywallSsoLoginUrl":"https://sso.immobilienscout24.de/sso/authenticate?appName=search&sso_return=https%3A%2F%2Fwww.immobilienscout24.de%2FSuche%2Fradius%2Fwohnung-mieten%3Fcenterofsearchaddress%3DGie%25C3%259Fen%2520%28Kreis%29%3B%3B%3B1276007006005%3B%3BGie%25C3%259Fen%3B%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383%3B8.67789%3B5.0%26enteredFrom%3Done_step_search&source=exclusivetimelabel","floodedListingMieterPlusBookingUrl":"/warenkorb/mieterplus/?returnUrl=https://www.immobilienscout24.de/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0%26enteredFrom%3DBUY_MPLUS&cmp_id=10-051727&cmp_name=residential_profile&cmp_position=residential_resultlist&cmp_creative=modal_paywall_cta","floodedListingKaueferPlusBookingUrl":"/warenkorb/kaeuferplus/?returnUrl=https://www.immobilienscout24.de/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0%26enteredFrom%3DBUY_KPLUS&cmp_id=10-051728&cmp_name=profile_buy_quickcheckout&cmp_position=residential_resultlist&cmp_creative=modal_paywall_cta","priceTabHomeOwnerWorldLoginUrl":"https://sso.immobilienscout24.de/sso/authenticate?appName=search&sso_return=https://www.immobilienscout24.de/meinkonto/meine-immobilien/&source=pricedevelopment"},"showPlusBookingModalFor":null,"landingPageDetails":null,"modifiedCriteriaCount":2,"mieterPlusUser":false,"priceInsightsEnabled":true,"kaeuferPlusUser":false},"cmsContent":{},"resultlist.resultlist":{"paging":{"next":{"@xlink.href":"\/Suche\/radius\/wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0&pagenumber=2"},"current":{"@xlink.href":"\/Suche\/radius\/wohnung-mieten?centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0"},"pageNumber":1,"pageSize":20,"numberOfPages":2,"numberOfHits":21,"numberOfListings":21},"searchId":"e9ba9473-0b55-3f8a-a5b0-6b676b425d2e","matchCountList":"","resultlistEntries":[{"@numberOfHits":"21","@realEstateType":"0","resultlistEntry":[{"@id":"147698275","@modification":"2023-11-28T20:01:08.118+01:00","@creation":"2023-11-28T20:05:22.840+01:00","@publishDate":"2023-11-28T20:05:22.840+01:00","realEstateId":147698275,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147698275","title":"Freundliche 3-Zimmer-Wohnung mit Einbauküche in Gießen","address":{"postcode":"35390","city":"Gießen (Kreis)","quarter":"Gießen","description":{"text":"Innenstadt, Gießen"}},"companyWideCustomerId":"001.20632178","floorplan":"false","streamingVideo":"false","listingType":"L","privateOffer":"true","contactDetails":{"salutation":"MALE","firstname":"Matthias","lastname":"Härtl","phoneNumber":"0176 56718659"},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/9065500a-0387-4cd3-acd6-caa9d7ee7ebc-1684709471.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ed6a4736-7849-4ca8-8022-e53528a3e0d0-1684709472.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/f0034c75-6c0f-40fb-812c-a01756fb508d-1684709473.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/34c091b0-842b-4943-b57e-5307238f98b9-1684709474.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bcdb6ea5-b984-40d2-9db0-195533a79750-1684709475.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/e0c9bc49-a05a-4e1d-bb89-23aa43155513-1684709476.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","paywallListing":{"active":"true"},"price":{"value":500,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":70,"numberOfRooms":3,"builtInKitchen":"true","balcony":"false","garden":"false","calculatedTotalRent":{"totalRent":{"value":880,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"500 €"},{"label":"Wohnfläche","value":"70 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":["Einbauküche","Keller","WG-geeignet"]},"hasNewFlag":"true"},{"@id":"147627798","@modification":"2023-11-24T08:35:51.566+01:00","@creation":"2023-11-03T11:28:22.000+01:00","@publishDate":"2023-11-03T11:28:22.000+01:00","realEstateId":147627798,"distance":0.39,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147627798","title":"In Gießens schönstem Viertel an der Wieseck: Offene 2 Zimmer-Maisonette-Wohnung mit Balkon, Löber...","address":{"street":"Löberstr.","houseNumber":"17a","postcode":"35390","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.58072,"longitude":8.67531},"preciseHouseNumber":"true","description":{"text":"Löberstr. 17a, Innenstadt, Gießen"}},"companyWideCustomerId":"001.17215","floorplan":"false","streamingVideo":"false","listingType":"L","privateOffer":"false","contactDetails":{"salutation":"NO_SALUTATION","firstname":"Claus R.","lastname":"Menges GmbH","company":"Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/e895c8cc-2d12-4d7f-9330-b3a249dab35e-1682406830.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/a35025ff-6399-4f56-8d02-6051e8f45973-1682406837.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/cb7c608a-44ab-4460-93f7-114488d833fa-1682406840.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/f1a5f200-f89c-4ad9-a1c0-96af01a8c052-1682406841.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/aaee8252-d0de-4601-b062-ca6ed882f40b-1682406842.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4cee33c4-be32-467c-af69-61af4f6719b3-1682406843.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/0269824f-202b-44d3-aa6c-e8306240181e-1682406844.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/274d8fed-9920-496f-acc1-2d7fec7fedbe-1682406863.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/a57c65eb-8b83-4a58-be8e-85f4cf874e63-1682406864.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/5bfaf1bf-2d75-4508-b40e-93f7dd289e0b-1682406866.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":680,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":68,"numberOfRooms":2,"energyPerformanceCertificate":"true","energyEfficiencyClass":"F","builtInKitchen":"true","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":930,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":1990},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"680 €"},{"label":"Wohnfläche","value":"68 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Einbauküche","Keller"]},"hasNewFlag":"false"},{"@id":"147677400","@modification":"2023-11-27T16:46:53.413+01:00","@creation":"2023-11-27T16:41:53.645+01:00","@publishDate":"2023-11-27T16:41:53.645+01:00","realEstateId":147677400,"distance":0.606,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147677400","title":"Walltorstraße 34, 35390 Gießen","address":{"street":"Walltorstraße","houseNumber":"34","postcode":"35390","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.58926,"longitude":8.67728},"preciseHouseNumber":"true","description":{"text":"Walltorstraße 34, Innenstadt, Gießen"}},"companyWideCustomerId":"001.19238817","floorplan":"false","streamingVideo":"false","listingType":"L","privateOffer":"true","contactDetails":{"salutation":"FEMALE","firstname":"Ceren","lastname":"Uygun"},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4c7ae478-5168-4a8e-ac6a-e525ef77766b-1684060867.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d708dd3d-dbdc-4987-b4e6-1bac63f6a822-1684060862.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/94e1e4d5-5997-4600-9d55-c20c35565f99-1684060853.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/95302e36-9181-47b2-82f8-87f922f418b9-1684060843.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ccb90651-c22f-481e-bb60-4007314c3cec-1684060799.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/60520a90-91fb-4f53-acc5-86169b7dd55d-1684060803.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2ccca4b3-cc73-43aa-a79f-0c8934dc9801-1684060870.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bc2af19a-0f1f-4621-a2fa-704b37282a02-1684060808.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c3157e6f-3338-4c61-90eb-086f5d70d233-1684060819.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/9f1228a1-5bcd-43e8-9535-c6ff24c441c0-1684060827.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/cfbd85ed-dab9-43d1-bcbb-fdb11551e0a6-1684060835.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/f0c8ffb0-942f-4121-99ac-6769fe88da00-1684071212.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/766ab9d9-a40b-4d1d-a61a-ccb91777f91d-1684060874.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/606ef35e-c110-4e1b-b1ee-e6ff3035309e-1684060797.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","paywallListing":{"active":"true"},"price":{"value":725,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":80,"numberOfRooms":3,"builtInKitchen":"false","balcony":"false","garden":"false","calculatedTotalRent":{"totalRent":{"value":1045,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"725 €"},{"label":"Wohnfläche","value":"80 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":["Keller","Gäste-WC","Aufzug"]},"hasNewFlag":"true"},{"@id":"139035681","@modification":"2023-11-21T16:02:24.542+01:00","@creation":"2023-01-13T14:17:37.000+01:00","@publishDate":"2023-01-13T14:17:37.000+01:00","realEstateId":139035681,"distance":0.949,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"139035681","title":"Nur für Gießener Senior:innen mit WBS: Großzügige 2 Zimmer-Wohnung mit Balkon - Sorglos leben in ...","address":{"street":"Curtmannstr.","houseNumber":"38","postcode":"35394","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.58548,"longitude":8.69108},"preciseHouseNumber":"true","description":{"text":"Curtmannstr. 38, Gießen-Ost, Gießen"}},"companyWideCustomerId":"001.17215","floorplan":"false","streamingVideo":"false","listingType":"L","privateOffer":"false","contactDetails":{"salutation":"NO_SALUTATION","firstname":"Claus R.","lastname":"Menges GmbH","company":"Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2021945b-9383-4521-af2f-43eb08c38078-1588840466.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/17ceb351-3058-40d9-b864-dc51d6d3c4c5-1588840468.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d20fd1fa-95c9-4155-9d21-7052a4d85c1a-1588840471.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/83046709-c52a-4360-a415-62f415ddee37-1588840474.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c0e787d5-6516-4379-bc53-c44b39278dc7-1588840476.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/71e27771-ce59-40c2-8803-ec1c52c80fea-1588840478.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/5172d3a4-5c17-40b5-bdfd-e8d3fdb6930b-1588840480.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/fd21df28-9e47-46b3-98d3-45af0a6e533b-1588840484.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/719e5a06-34cd-4132-8df6-1d3f74f30f98-1588840488.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":335,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":64,"numberOfRooms":2,"energyPerformanceCertificate":"true","energyEfficiencyClass":"C","builtInKitchen":"false","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":665,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":1986},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"335 €"},{"label":"Wohnfläche","value":"64 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Keller"]},"hasNewFlag":"false"},{"@id":"147564321","@modification":"2023-11-20T16:37:05.184+01:00","@creation":"2023-11-20T16:36:01.000+01:00","@publishDate":"2023-11-20T16:36:01.000+01:00","realEstateId":147564321,"distance":1.057,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147564321","title":"Mit gleich 2 Balkonen! Lichtdurchflutete, moderne und attraktive 2 Zimmer-Wohnung Nähe Bahnhof+In...","address":{"street":"Schuppstr.","houseNumber":"1","postcode":"35398","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.582,"longitude":8.6632},"preciseHouseNumber":"true","description":{"text":"Schuppstr. 1, Gießen-Süd, Gießen"}},"companyWideCustomerId":"001.17215","floorplan":"false","streamingVideo":"false","listingType":"L","privateOffer":"false","contactDetails":{"salutation":"NO_SALUTATION","firstname":"Claus R.","lastname":"Menges GmbH","company":"Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f05c9994-2f3f-48f5-b577-0bbf0517d45e.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"Claus R. Menges GmbH Immobilienvermittlung und Hausverwaltung","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/4fa876a5-2d2f-4ef5-b268-0e3ee850c833.PNG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/8f7263a2-95ca-407c-85dd-4e34cc947952-1680196820.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/f15c7270-1ee5-48ca-b950-ff0ddda1cc52-1680196823.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/dfa37c2b-b8fc-4952-9dab-9d22a27495a3-1680196826.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/7c6b2a34-10b5-4f91-8dd0-196f2b358679-1680196827.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":730,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":54,"numberOfRooms":2,"energyPerformanceCertificate":"true","energyEfficiencyClass":"A","builtInKitchen":"true","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":975,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":2019},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"730 €"},{"label":"Wohnfläche","value":"54 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Einbauküche","Keller","Aufzug"]},"hasNewFlag":"true"},{"@id":"138407506","@modification":"2023-11-23T22:56:28.842+01:00","@creation":"2023-11-23T22:58:00.000+01:00","@publishDate":"2023-11-23T22:58:00.000+01:00","realEstateId":138407506,"distance":1.565,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"138407506","title":"Bezahlbare 3-Zi-Wohnung mit Balkon","address":{"street":"Marburger Str.","houseNumber":"86","postcode":"35396","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.59729,"longitude":8.6844},"preciseHouseNumber":"true","description":{"text":"Marburger Str. 86, Gießen-Nord, Gießen"}},"companyWideCustomerId":"001.12607949","floorplan":"false","streamingVideo":"false","listingType":"L","privateOffer":"false","contactDetails":{"salutation":"NO_SALUTATION","lastname":"Ihr Vermietungsteam der Sucasa ","company":"sucasa e.K.","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"sucasa e.K.","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/b9800be2-5c4a-429c-9aa8-c41f65e2db52.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/0f3348ac-c493-48a2-8a07-cce22c67e9e3-1582183031.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/8eb48d11-f659-427d-bf5b-c9a753e532d5-1582183226.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/87882819-ac44-4615-ae48-7481905922ac-1621582961.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ec925094-23f8-41f1-be8b-83739bbea1ff-1582183308.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/a6a4517c-2350-48ed-88e1-5ce8166f28a5-1621582967.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/9bcfad74-68ef-4085-b2af-0e6f483ced6a-1582183579.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/9d9144ec-103e-48f5-8a4a-f692d0e4e64d-1621582971.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d78c663a-c47d-4a96-805d-6db0fbbd6754-1582183434.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/f8b9afea-b4c4-4b53-b2f4-80a26f749bbe-1582183371.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d7c5e8ed-0520-45d5-a79c-132210b905a7-1621582978.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/eb5043bc-6c62-4007-87b6-4beef89fbf35-1582183484.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/92796381-7f6d-42f5-a7e3-2716b7c3f97e-1621582985.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/8d74427e-199d-44d1-92bc-6428bbaf5bfe-1582183514.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/60d5531f-adae-4a74-98af-e68b73fb57f8-1582183616.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":750,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":78,"numberOfRooms":3,"builtInKitchen":"false","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":1070,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"750 €"},{"label":"Wohnfläche","value":"78 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Gäste-WC","Aufzug","WG-geeignet"]},"hasNewFlag":"true"},{"@id":"147463951","@modification":"2023-11-24T09:23:36.396+01:00","@creation":"2023-11-16T15:31:17.000+01:00","@publishDate":"2023-11-16T15:31:17.000+01:00","realEstateId":147463951,"distance":2.037,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147463951","title":"frisch sanierte Wohnung am Stadtrand","address":{"street":"Eichendorffring","houseNumber":"137","postcode":"35394","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.58177,"longitude":8.70657},"preciseHouseNumber":"true","description":{"text":"Eichendorffring 137, Gießen-Ost, Gießen"}},"companyWideCustomerId":"001.403897","floorplan":"false","streamingVideo":"false","listingType":"L","privateOffer":"false","contactDetails":{"salutation":"MALE","firstname":"Marcus ","lastname":"Gehrhardt","phoneNumber":"0641 943770","company":"Erich Ries Immobilien- und Verwaltungs GmbH"},"realtorCompanyName":"Erich Ries Immobilien- und Verwaltungs GmbH","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/0657fe8d-22fc-4107-ad58-e8483ed68f16.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ca4e064f-a24e-4fe7-a1a5-e472c6bc3290-1678169429.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c7f97afa-de7a-497f-b2cb-c962305bca68-1678349230.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d22933f1-3108-43ec-a1a4-b074d4b0daf9-1678160456.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/72d95a81-c521-4566-b466-886969cdc5d0-1678160403.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/576219ee-0099-4748-903e-13822a490902-1678160513.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/6509553b-e7eb-49c0-9cbe-295b4dc81c56-1678160555.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/b8a1caaa-fd9e-4e3f-ac2d-fd8746c66c16-1678160675.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/71263bf2-4e01-4cdf-acb6-dd45b57d5059-1678160739.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/aaa8246d-0aae-42c3-86ec-67f784a56c36-1678160894.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bf85c057-a3bf-4521-b634-4ba8ea1c1b1b-1678160289.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/126b7795-aef2-4811-a0a1-0e519b804c58-1678160380.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":670,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":75,"numberOfRooms":3,"energyPerformanceCertificate":"true","builtInKitchen":"false","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":920,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":1964},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"670 €"},{"label":"Wohnfläche","value":"75 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Keller","Aufzug"]},"hasNewFlag":"true"},{"@id":"129475294","@modification":"2023-11-16T14:46:20.872+01:00","@creation":"2023-11-15T11:02:47.000+01:00","@publishDate":"2023-11-15T11:02:47.000+01:00","realEstateId":129475294,"distance":4.912,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"129475294","title":"Ruhige und günstige 3-ZKB Dachgeschosswohnung, 2-er WG geeignet","address":{"street":"Jägerschneise","houseNumber":"4","postcode":"35440","city":"Gießen (Kreis)","quarter":"Linden","wgs84Coordinate":{"latitude":50.54102,"longitude":8.66067},"preciseHouseNumber":"true","description":{"text":"Jägerschneise 4, Linden, Gießen (Kreis)"}},"companyWideCustomerId":"001.12607949","floorplan":"false","streamingVideo":"true","listingType":"L","privateOffer":"false","contactDetails":{"salutation":"NO_SALUTATION","lastname":"Ihr Vermietungsteam der Sucasa ","company":"sucasa e.K.","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/f20a0fe6-7d56-4c73-bea6-b259146dda06.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"sucasa e.K.","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/b9800be2-5c4a-429c-9aa8-c41f65e2db52.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/be650aad-5fef-4343-8557-c6405e0d0f79-1489354353.png\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/67bedf7d-d6d3-405a-bc90-8903c1be2082-1489354247.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1daa098e-7286-4b00-b6f8-4ca9e5806f91-1489354228.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/847b7311-a8cf-4986-a961-33497268bf80-1489354298.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d0291975-36c8-4a7b-bccd-2325f83895e2-1489354271.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/89add1d4-966c-481b-88c8-512814b71ade-1489354332.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/b5357ed2-9b12-4d82-9e8c-75670f9dbb8f-1469057670.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/280e7fb0-d4de-4255-bb80-9bdb1948e5c8-1469057538.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/f7eb2244-8023-4f81-996b-2e7da4155bca-1469057577.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4dccc3c1-4726-4bb8-84bd-ec939c954f0f-1469057597.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2d3383ec-6079-46ff-9c8c-a0905fbf6584-1469057554.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4738df3f-0d0c-47ae-a88e-2bb1b0d616e9-1469057572.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2c45fd6f-91d4-4fba-954a-edb1ecba23c7-1480200246.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/0b499c00-ccce-42c0-8164-d73d35563bce-1469057690.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ba5a76bb-e974-443b-8f8a-e7d9ad8e9e68-1469057745.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/a0013756-2796-4f08-9a6b-470319b54a01-1489354259.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:StreamingVideo","videoId":"iTlk3U9nLHF-5bn78WcjoQ"}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":680,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":80,"numberOfRooms":3,"builtInKitchen":"true","balcony":"true","garden":"true","calculatedTotalRent":{"totalRent":{"value":860,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"680 €"},{"label":"Wohnfläche","value":"80 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Einbauküche","Garten","WG-geeignet"]},"hasNewFlag":"true"},{"@id":"113185270","@modification":"2023-11-24T11:07:49.268+01:00","@creation":"2023-11-23T15:28:37.000+01:00","@publishDate":"2023-11-23T15:28:37.000+01:00","realEstateId":113185270,"distance":0.462,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"113185270","title":"2 Zimmerwohnung, Uni-nah","address":{"street":"Stephanstraße","houseNumber":"23","postcode":"35390","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.57969,"longitude":8.67865},"preciseHouseNumber":"true","description":{"text":"Stephanstraße 23, Innenstadt, Gießen"}},"companyWideCustomerId":"001.5377865","floorplan":"false","streamingVideo":"false","listingType":"M","privateOffer":"false","contactDetails":{"salutation":"FEMALE","firstname":"Cornelia ","lastname":"Wallenfels","phoneNumber":"0174 3570090","company":"Lang GmbH & Co. KG","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/5f5a98cf-7e69-47c5-9971-15df082a0d2d.JPG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/5f5a98cf-7e69-47c5-9971-15df082a0d2d.JPG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/5f5a98cf-7e69-47c5-9971-15df082a0d2d.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/5f5a98cf-7e69-47c5-9971-15df082a0d2d.JPG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/5f5a98cf-7e69-47c5-9971-15df082a0d2d.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"Lang GmbH & Co. KG","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/e38fe9f9-ce6a-4096-a922-19cdcd451bd7.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/7b097051-f963-4c34-9848-f5f4437294e4-1315134339.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/6934722c-0535-479e-88c1-3c1e56f290d5-1315134341.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/fffe1b93-7049-4a87-8d38-5cc0cd4ae1ac-1315135263.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":540,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":56.75,"numberOfRooms":2,"energyPerformanceCertificate":"true","builtInKitchen":"false","balcony":"false","garden":"false","calculatedTotalRent":{"totalRent":{"value":740,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":1956},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"540 €"},{"label":"Wohnfläche","value":"56,75 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":"Keller"},"hasNewFlag":"true"},{"@id":"147616510","@modification":"2023-11-23T13:36:10.516+01:00","@creation":"2023-11-23T13:36:14.000+01:00","@publishDate":"2023-11-23T13:36:14.000+01:00","realEstateId":147616510,"distance":0.542,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147616510","title":"Erstbezug im Herzen Gießens","address":{"street":"Walltorstraße","houseNumber":"16","postcode":"35390","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.5886,"longitude":8.67638},"preciseHouseNumber":"true","description":{"text":"Walltorstraße 16, Innenstadt, Gießen"}},"companyWideCustomerId":"002.01009270899","floorplan":"false","streamingVideo":"false","listingType":"M","privateOffer":"false","contactDetails":{"salutation":"FEMALE","firstname":"Lea","lastname":"Burk","phoneNumber":"01515 5919310","cellPhoneNumber":"01515 5919310","company":"Real Estate Service Hartmann & Burk GbR"},"realtorCompanyName":"Real Estate Service Hartmann & Burk GbR","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/ce57c77c-2ddf-485d-9650-f006b1803ab4.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/9806e768-d3ba-452a-83fe-aa059dae2616-1681897145.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2bc34587-5be3-4803-8e20-d4f2ed2e4a21-1681897104.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d509d1b2-a9ab-46a6-84df-23ae06001af7-1681897142.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bb83871e-6e55-4bd0-8938-7a671ff4221a-1681897098.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/028738e9-4052-43b1-bccc-4bddb7cf582a-1681897102.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/40480a0d-ba53-4db0-bde2-65b0b372d3a1-1681897125.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":739,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":57,"numberOfRooms":2,"builtInKitchen":"false","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":829,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":2023},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"739 €"},{"label":"Wohnfläche","value":"57 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","WG-geeignet"]},"hasNewFlag":"true"},{"@id":"147638484","@modification":"2023-11-24T15:56:50.087+01:00","@creation":"2023-11-24T15:53:48.000+01:00","@publishDate":"2023-11-24T15:53:48.000+01:00","realEstateId":147638484,"distance":0.557,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147638484","title":"Frisch sanierte 2,5-Zimmer-Wohnung in Gießen","address":{"street":"Lessingstraße","houseNumber":"4","postcode":"35390","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.57882,"longitude":8.67754},"preciseHouseNumber":"true","description":{"text":"Lessingstraße 4, Innenstadt, Gießen"}},"companyWideCustomerId":"002.01005507036","floorplan":"false","streamingVideo":"false","listingType":"M","privateOffer":"false","contactDetails":{"salutation":"FEMALE","firstname":"Evelina","lastname":"Drobik","company":"WEVATO GmbH"},"realtorCompanyName":"WEVATO GmbH","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/3fdc9491-128d-4f68-a5a0-59cdca908f76.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/fcda86a7-125b-4b37-bf53-2411d369ced6-1682610295.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/fe514e92-231e-4375-af9d-ad723f558455-1682610914.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4c60c06a-f4a9-472f-8324-552620d2e2ad-1682610882.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/019ae2d2-af19-423f-ac2c-edac5418c979-1682610953.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/b5ed70f8-6da3-4731-94b4-8f8df81e3104-1682610945.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1295d25b-e2ad-4b16-9943-a2795d395eb2-1682610869.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":535,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":53.93,"numberOfRooms":2,"energyPerformanceCertificate":"true","builtInKitchen":"false","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":820,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":1962},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"535 €"},{"label":"Wohnfläche","value":"53,93 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Keller","WG-geeignet"]},"hasNewFlag":"true"},{"@id":"126716839","@modification":"2023-11-27T11:11:25.107+01:00","@creation":"2023-11-27T11:11:41.000+01:00","@publishDate":"2023-11-27T11:11:41.000+01:00","realEstateId":126716839,"distance":1.078,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"126716839","title":"Neubau am Kugelberg in Gießen - hier: Penthouse 2 Zi. Whg. mit Dachterrasse und Wohnküche, inkl. EBK","address":{"street":"Lärchenwäldchen","houseNumber":"7","postcode":"35394","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.58406,"longitude":8.69317},"preciseHouseNumber":"true","description":{"text":"Lärchenwäldchen 7, Gießen-Ost, Gießen"}},"companyWideCustomerId":"002.01010007243","floorplan":"true","streamingVideo":"false","listingType":"M","privateOffer":"false","contactDetails":{"salutation":"FEMALE","firstname":"Judith Radtke","lastname":"IBG Immobilienbetreuung GmbH ","phoneNumber":"06421 8890469","cellPhoneNumber":"01516 2385581","company":"FIVE STAR Investment GmbH","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/21520ea4-d553-4010-9c39-a9a753d39d02.JPG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/21520ea4-d553-4010-9c39-a9a753d39d02.JPG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/21520ea4-d553-4010-9c39-a9a753d39d02.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/21520ea4-d553-4010-9c39-a9a753d39d02.JPG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/21520ea4-d553-4010-9c39-a9a753d39d02.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"FIVE STAR Investment GmbH","galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"true","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1390a2a1-04a7-4036-9817-3b2063cbbdba-1429775907.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"true","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c9f93788-fb97-4b4f-91f9-fa07ecd49a96-1429775949.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/664ef5b6-02a4-4dc4-bf5c-7fa9a4b8a723-1683957351.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/695ce2d7-d644-4482-9752-82bdb6812f19-1683957425.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1b2c34c9-f6ce-40ed-88ec-649239d2c3de-1683957211.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/7382087d-ba72-4db8-88ec-36b1003a872a-1683957213.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2cb4ae5e-147d-45f5-9524-ac829f6afda9-1683957218.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":583,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":45.19,"numberOfRooms":2,"builtInKitchen":"true","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":894,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":2017},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"583 €"},{"label":"Wohnfläche","value":"45,19 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Einbauküche","Keller","Aufzug","Stufenlos"]},"hasNewFlag":"true"},{"@id":"147308685","@modification":"2023-11-23T14:59:00.944+01:00","@creation":"2023-11-08T15:05:23.000+01:00","@publishDate":"2023-11-08T15:05:23.000+01:00","realEstateId":147308685,"distance":2.896,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147308685","title":"Moderne Dachgeschosswohnung in zentraler Lage","address":{"street":"Eisenstein","houseNumber":"4","postcode":"35396","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.6067,"longitude":8.69752},"preciseHouseNumber":"true","description":{"text":"Eisenstein 4, Wieseck, Gießen"}},"companyWideCustomerId":"002.01008207922","floorplan":"false","streamingVideo":"false","listingType":"M","privateOffer":"false","contactDetails":{"salutation":"MALE","firstname":"Mike","lastname":"Biehl","company":"Kirchmann Immobilienvermittlung GmbH"},"realtorCompanyName":"Kirchmann Immobilienvermittlung GmbH","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/fc2f3c51-6bcf-4e3d-8bac-b308b3b28d7b.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2e4dccba-5e7d-4d1a-81bb-b9305cc1a161-1673892425.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/f79a089d-83c2-48dc-b483-dc86805bbadf-1673892427.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c176b4a0-a63e-4597-ae93-8d65b3505218-1673892431.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1b3715b8-ef75-4b26-ac68-3c4585639105-1673892434.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/a9f88506-7a6a-4e24-bdef-4a261318c71d-1673892440.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/43bbf722-1b6d-4a47-a130-44fbce06da2a-1673892445.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1d63383c-7379-467b-ae78-f90c36c78bb6-1673892453.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/6e66e79b-29d6-46fb-8d22-b5352a409fda-1673892461.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/b5904879-4a7a-400b-be81-4ed79cffc8d1-1673892471.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1edbb5c9-4be3-43cd-9642-8613b12849b6-1673892480.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c3bf7ba8-be41-4a65-8f24-847291714ae1-1673892485.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","price":{"value":800,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":68,"numberOfRooms":3,"builtInKitchen":"false","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":1020,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"800 €"},{"label":"Wohnfläche","value":"68 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":"Balkon\/Terrasse"},"hasNewFlag":"false"},{"@id":"136625278","@modification":"2023-11-27T13:08:51.685+01:00","@creation":"2023-11-27T13:08:53.000+01:00","@publishDate":"2023-11-27T13:08:53.000+01:00","realEstateId":136625278,"distance":3.098,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"136625278","title":"Moderne 2-Zimmer-Wohnung mit Balkon","address":{"street":"Fockestraße","houseNumber":"2","postcode":"35394","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.59189,"longitude":8.7199},"preciseHouseNumber":"true","description":{"text":"Fockestraße 2, Gießen-Ost, Gießen"}},"companyWideCustomerId":"002.01008207922","floorplan":"true","streamingVideo":"false","listingType":"M","privateOffer":"false","contactDetails":{"salutation":"MALE","firstname":"Mike","lastname":"Biehl","company":"Kirchmann Immobilienvermittlung GmbH"},"realtorCompanyName":"Kirchmann Immobilienvermittlung GmbH","realtorLogoForResultList":{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/fc2f3c51-6bcf-4e3d-8bac-b308b3b28d7b.JPG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"}}]},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/404be2ab-0c07-4178-8f05-4ef4a7ce76c9-1561999748.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1c17fbb0-0402-4713-8f63-160dbe281db2-1561999754.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/71c87f8d-4ae2-4c82-83ce-98f724f42652-1561999758.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bc4ed4db-17ca-4541-b273-68b89c222448-1561999764.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2050e659-e4a0-4395-933e-26f529659df9-1561999769.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/9ac85264-c712-4d92-92fd-d8fa8d7929ad-1561999776.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/454522e8-c415-436f-ab54-797563a3cc0a-1561999784.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bad6f180-8e03-492a-8724-513c1533a548-1561999789.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/a53b08bc-c2aa-4fd4-8b1e-7c7586f9eff4-1561999795.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d6d9e10c-a981-4c35-a9c7-6b1cd8f6c3af-1561999798.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"true","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/43b5e90a-9bf2-4660-ade3-aa9c5317fe6e-1561999802.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","price":{"value":770,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":64,"numberOfRooms":2,"builtInKitchen":"false","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":910,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":2020},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"770 €"},{"label":"Wohnfläche","value":"64 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Aufzug"]},"hasNewFlag":"true"},{"@id":"147637654","@modification":"2023-11-24T15:16:46.420+01:00","@creation":"2023-11-24T15:20:46.969+01:00","@publishDate":"2023-11-24T15:20:46.969+01:00","realEstateId":147637654,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147637654","title":"Zwischenmiete! Für 3 Monate in geräumiger Wohnung mit guter Lage","address":{"postcode":"35392","city":"Gießen (Kreis)","quarter":"Gießen","description":{"text":"Innenstadt, Gießen"}},"companyWideCustomerId":"001.20618702","floorplan":"false","streamingVideo":"false","listingType":"S","privateOffer":"true","contactDetails":{"salutation":"FEMALE","firstname":"Juliette","lastname":"Wismar"},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/0d5cc572-8c3b-443a-b034-f3b1b470567b-1682587046.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/38b0c174-6e6d-43b4-bc48-5f5c372862db-1682587043.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/e34f3e0f-5981-4611-a461-bd2cb33748a9-1682587033.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/cd6ade5d-4b3d-4425-92e2-97ea1e39ab23-1682587036.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/7dd68396-ebc6-4077-bb93-ec3ae695fe8a-1682587039.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d5fe8c65-8f6c-448b-bc05-d3a345a09c11-1682587040.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4f7de339-e4f8-40e5-a337-bc450dd7fdd9-1682587047.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/5c5e42ca-471c-4885-9c72-f458ea8f61a5-1682587049.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/7a3a446f-5932-46c8-8bfd-d7c9de996c10-1682587053.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/6e44e6c3-3b8e-4533-b435-f03daa3da8b1-1682587054.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","paywallListing":{"active":"true"},"price":{"value":600,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":59,"numberOfRooms":2.5,"builtInKitchen":"true","balcony":"false","garden":"true","calculatedTotalRent":{"totalRent":{"value":700,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"600 €"},{"label":"Wohnfläche","value":"59 m²"},{"label":"Zimmer","value":"2,5"}]}],"realEstateTags":{"tag":["Einbauküche","Garten","Keller"]},"hasNewFlag":"true"},{"@id":"146396243","@modification":"2023-11-12T16:55:15.074+01:00","@creation":"2023-10-04T15:05:10.000+02:00","@publishDate":"2023-10-04T15:05:10.000+02:00","realEstateId":146396243,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"146396243","title":"Sanierte Dachterrassenwohnung im 2 Fam. Haus \/ Anneröder Siedlung","address":{"postcode":"35394","city":"Gießen (Kreis)","quarter":"Gießen","description":{"text":"Gießen-Ost, Gießen"}},"companyWideCustomerId":"001.503799","floorplan":"false","streamingVideo":"false","listingType":"S","privateOffer":"false","contactDetails":{"salutation":"MALE","firstname":"Stefan","lastname":"Sahl","phoneNumber":"0641 6869990","cellPhoneNumber":"0170 7387033","company":"Stefan Sahl Immobilien","portraitUrl":"https:\/\/pictures.immobilienscout24.de\/usercontent\/ffedcad3-2007-4e96-98ff-4f893025d8b4.JPEG","portraitUrlForResultList":{"@xsi.type":"common:Picture","@xlink.href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/ffedcad3-2007-4e96-98ff-4f893025d8b4.JPEG","floorplan":"false","titlePicture":"false","urls":[{"url":[{"@scale":"SCALE","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/ffedcad3-2007-4e96-98ff-4f893025d8b4.JPEG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/quality\/50"},{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/ffedcad3-2007-4e96-98ff-4f893025d8b4.JPEG\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"},{"@scale":"WHITE_FILLING","@href":"https:\/\/pictures.immobilienscout24.de\/usercontent\/ffedcad3-2007-4e96-98ff-4f893025d8b4.JPEG\/ORIG\/resize\/%WIDTH%x%HEIGHT%%3E\/extent\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}]}]}},"realtorCompanyName":"Stefan Sahl Immobilien","galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/3fd42eea-ab9a-4333-b679-27d9f1857d54-1675969201.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/5c925e70-e54f-4a02-a1b6-74215bf44f4e-1675969203.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/39b87268-7373-4a16-89cd-a50f3ea26c32-1675969205.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/26aff186-fec3-4a0d-94ae-5a853bccd759-1675969207.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/135440f3-b16d-4a4c-92cf-28cbb85e274f-1675969209.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/69970ad6-f6b2-4c3b-82d9-08cdce6323ca-1675969211.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","verifiedBy":["TNS_REALTOR_BADGE"],"price":{"value":695,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":81,"numberOfRooms":2,"energyPerformanceCertificate":"true","builtInKitchen":"false","balcony":"false","garden":"false","calculatedTotalRent":{"totalRent":{"value":960,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"ESTIMATED"},"constructionYear":1954},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"695 €"},{"label":"Wohnfläche","value":"81 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":"","hasNewFlag":"false"},{"@id":"147659700","@modification":"2023-11-26T16:13:04.628+01:00","@creation":"2023-11-26T16:15:20.561+01:00","@publishDate":"2023-11-26T16:15:20.561+01:00","realEstateId":147659700,"distance":2.222,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147659700","title":"2-Zimmer-EG-Wohnung mit Balkon und Einbauküche in Gießen","address":{"street":"Heinrich-Ritzel-Straße","houseNumber":"2","postcode":"35396","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.59887,"longitude":8.69861},"preciseHouseNumber":"true","description":{"text":"Heinrich-Ritzel-Straße 2, Wieseck, Gießen"}},"companyWideCustomerId":"001.20537015","floorplan":"false","streamingVideo":"false","listingType":"S","privateOffer":"true","contactDetails":{"salutation":"FEMALE","firstname":"Karola","lastname":"Schmidt"},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4299e752-ec0d-428c-824a-6da79203a44d-1683559293.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/174b3d19-3b71-478b-8459-d866c1b1d2ca-1683559295.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/dd73621e-1956-4c8d-9374-d6f659db5f5d-1683559297.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d5bc4059-6754-4c85-845f-ca0a04b31a64-1683559303.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/da42cc03-93c3-45a5-8a5d-9262b4ccf0d9-1683559304.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/3592dc97-c650-4518-93ea-d02f91b06947-1683559305.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/be7a051e-c95d-40bd-a75d-658259bc0c0b-1683559307.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/7dc800fa-0695-40ed-96b5-63891eae9083-1683559308.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","paywallListing":{"active":"true"},"price":{"value":550,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":44,"numberOfRooms":2,"builtInKitchen":"true","balcony":"true","garden":"true","calculatedTotalRent":{"totalRent":{"value":670,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"550 €"},{"label":"Wohnfläche","value":"44 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Einbauküche","Garten","Keller"]},"hasNewFlag":"true"},{"@id":"147283283","@modification":"2023-11-07T12:32:52.642+01:00","@creation":"2023-11-07T12:32:33.000+01:00","@publishDate":"2023-11-07T12:32:33.000+01:00","realEstateId":147283283,"distance":2.593,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147283283","title":"Helle freundliche 3 ZKB Wohnung mit Küchenzeile (1501-5016)","address":{"street":"Ludwig-Schneider-Weg","houseNumber":"1-7","postcode":"35398","city":"Gießen (Kreis)","quarter":"Gießen","wgs84Coordinate":{"latitude":50.58781,"longitude":8.64171},"preciseHouseNumber":"true","description":{"text":"Ludwig-Schneider-Weg 1-7, Gießen-West, Gießen"}},"companyWideCustomerId":"001.5361688","floorplan":"false","streamingVideo":"false","listingType":"S","privateOffer":"false","contactDetails":{"salutation":"NO_SALUTATION","firstname":"Sandra","lastname":"Schäfer","company":"Finas GmbH & Co. KG"},"realtorCompanyName":"Finas GmbH & Co. KG","galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d9ea8fea-1d31-4fd8-80db-f0d6ab9386fb-1673189724.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/eb10d44d-ec41-46dc-bd68-62a1dd0d6ad3-1673189728.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/cd771d25-9932-4227-aa65-a1c4976ce6f4-1673189738.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/98e8ace7-e658-432b-a2cc-8505cdba04f7-1673189741.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ceabefc7-b8fd-4144-afe0-d30582c76436-1673189743.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bf2ed922-9039-4be9-a180-39ab591e37ce-1673189744.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ed7e1e5c-fd4b-4d9b-8072-6bcd751535e6-1673189746.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/98b31979-9e1a-4352-b284-d69380a9802f-1673189747.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/9934cb47-ec05-474f-9051-510a064c3538-1673189749.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/cce3752d-8635-4b54-afed-8e9c16a54731-1673189752.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/cd02c2f8-d461-4af3-9188-0c7e56e42286-1673189755.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/01fbdeb8-99fc-481c-9cf8-3ac4736a1fa2-1673189757.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/be5dce5a-23b1-4418-944f-497db3d8bd76-1673189759.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/a5b7ed60-754a-4d93-8db0-8771b695f913-1673189763.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/4c7f7272-2e43-4e96-a908-e0ab33f29ba3-1673189765.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/32c1be1d-c356-4ef9-8414-952e67ea74b7-1673189768.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/380e536c-a1f1-4adf-9de3-8e277fc3620f-1673189770.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/d4a9f8b3-9e38-4dff-ab2f-fe062028f688-1673189772.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/2572bc4b-5821-4728-b4fa-df9c44b6ef10-1673189774.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","price":{"value":800,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":87,"numberOfRooms":3,"energyPerformanceCertificate":"true","energyEfficiencyClass":"C","builtInKitchen":"true","balcony":"false","garden":"false","calculatedTotalRent":{"totalRent":{"value":1040,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"},"constructionYear":1997},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"800 €"},{"label":"Wohnfläche","value":"87 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":"Einbauküche"},"hasNewFlag":"false"},{"@id":"140712013","@modification":"2023-11-26T11:09:54.570+01:00","@creation":"2023-11-27T13:31:13.000+01:00","@publishDate":"2023-11-27T13:31:13.000+01:00","realEstateId":140712013,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"140712013","title":"2-Zimmer-Wohnung mit Balkon in Giessen-Wieseck","address":{"postcode":"35396","city":"Gießen (Kreis)","quarter":"Gießen","description":{"text":"Wieseck, Gießen"}},"companyWideCustomerId":"001.19742205","floorplan":"false","streamingVideo":"false","listingType":"S","privateOffer":"true","contactDetails":{"salutation":"MALE","firstname":"Christoph","lastname":"Schultze"},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/b5b61b8f-e1e2-4400-b526-b568a5321fec-1674550381.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/da2f3290-0bad-457f-ad56-99c31824b1b8-1674550384.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1fd7f0a9-6fed-43aa-be1f-6dcbe1cea944-1674550386.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/b6dbdd03-a02f-46f2-9ac1-414f10a56426-1674550389.jpg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","paywallListing":{"active":"true"},"price":{"value":480,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":46,"numberOfRooms":2,"builtInKitchen":"true","balcony":"true","garden":"false","calculatedTotalRent":{"totalRent":{"value":630,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"480 €"},{"label":"Wohnfläche","value":"46 m²"},{"label":"Zimmer","value":2}]}],"realEstateTags":{"tag":["Balkon\/Terrasse","Einbauküche","Keller"]},"hasNewFlag":"true"},{"@id":"147470506","@modification":"2023-11-15T21:23:18.246+01:00","@creation":"2023-11-15T21:24:06.634+01:00","@publishDate":"2023-11-15T21:24:06.634+01:00","realEstateId":147470506,"disabledGrouping":"false","resultlist.realEstate":{"@xsi.type":"search:ApartmentRent","@id":"147470506","title":"Schöne 3-Zimmer-Wohnung zur Miete in 35435, Wettenberg","address":{"postcode":"35435","city":"Gießen (Kreis)","quarter":"Wettenberg","description":{"text":"Wettenberg, Gießen (Kreis)"}},"companyWideCustomerId":"009.1abb5c94-cf4a-4f13-8cc8-c434c66778a3","floorplan":"false","streamingVideo":"false","listingType":"S","privateOffer":"true","contactDetails":{"salutation":"NO_SALUTATION","lastname":"Alpin"},"galleryAttachments":{"attachment":[{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/bd1e5811-d931-4475-a8d0-e6a9f8902d5f-1677894286.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1318aed3-6e11-441f-840d-a8dcca5a69df-1677894290.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/eb3803b6-f5c8-43fe-90be-afd0a55c7c91-1677894295.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/18391fb0-f512-49dc-a564-27010ef44700-1677894294.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/1f36ed21-dcc2-4fc1-827a-bcdfc0331a45-1677894289.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c922a980-d03f-437f-b64b-35607ffa70ba-1677894287.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/c6cf9863-d100-4b30-88ff-65918f87d5f1-1677894291.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/aed4c692-5187-48fd-ad3e-00d037051788-1677894292.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]},{"@xsi.type":"common:Picture","floorplan":"false","titlePicture":"false","urls":[{"url":{"@scale":"SCALE_AND_CROP","@href":"https:\/\/pictures.immobilienscout24.de\/listings\/ead79648-0a28-4593-9ed2-b40fb0ae236d-1677894296.jpeg\/ORIG\/legacy_thumbnail\/%WIDTH%x%HEIGHT%\/format\/webp\/quality\/50"}}]}]},"spotlightListing":"false","paywallListing":{"active":"true"},"price":{"value":800,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"livingSpace":95,"numberOfRooms":3,"builtInKitchen":"true","balcony":"false","garden":"false","calculatedTotalRent":{"totalRent":{"value":1000,"currency":"EUR","marketingType":"RENT","priceIntervalType":"MONTH"},"calculationMode":"SUMMARIZED"}},"attributes":[{"attribute":[{"label":"Kaltmiete","value":"800 €"},{"label":"Wohnfläche","value":"95 m²"},{"label":"Zimmer","value":3}]}],"realEstateTags":{"tag":["Einbauküche","Keller"]},"hasNewFlag":"true"}]}],"description":{"text":"Mietwohnung, im Umkreis von 5 km von Gießen (Kreis), ab 2 Zimmer, bis 800 € Kaltmiete"}}}},
      isUserLoggedIn: false,
      nonceToken: "74366215b159175f22c44ab94b6eec7a",
      resultListQueryUrlTemplate: "/Suche/controller/mapResults.go?searchUrl=/Suche/radius/wohnung-mieten?centerofsearchaddress%3DGie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;%26numberofrooms%3D2.0-%26price%3D-800.0%26pricetype%3Drentpermonth%26geocoordinates%3D50.58383;8.67789;5.0&pageSize=%pageSize%",
      lastSearchApiUrl: "/radius?realestatetype=apartmentrent&centerofsearchaddress=Gie%C3%9Fen%20(Kreis);;;1276007006005;;Gie%C3%9Fen;&numberofrooms=2.0-&price=-800.0&pagesize=20&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0&pagenumber=1"
    };

    
    document._open = document.open;
    document.open = function () {
      return document;
    };

    
    picsearch_ajax_auth = "QPfd1JLlHHPH1XPNv3Rxha_2CbGAk0PfgLeg_FPn1FNeg_zJUv_eKw";

    window.maps_callback = function () {};

    var utag_data = utag_data || {};
    utag_data.KVrooms = "2.0";
    utag_data.query_regio2 = "gießen_kreis";
    utag_data.query_regio1 = "hessen";
    utag_data.query_numberOfRoomsMin = "2.0";
    utag_data.query_numberOfRoomsAvg = "2.0";
    utag_data.ga_cd_cxp_referrer = "ONE_STEP_SEARCH";
    utag_data.geo_ot = "innenstadt";
    utag_data.query_regio4 = "innenstadt";
    utag_data.query_regio3 = "gießen";
    utag_data.obj_ityp = "Wohnung_Miete";
    utag_data.geo_land = "deutschland";
    utag_data.KVimmotype = "APARTMENT_RENT";
    utag_data.timestamp = "11.2023";
    utag_data.query_radius = "5.0";
    utag_data.query_realEstateType = "APARTMENT_RENT";
    utag_data.obj_resultlist_count = "21";
    utag_data.obj_crosstype = "liv_apartment_rent";
    utag_data.geo_bln = "hessen";
    utag_data.KVcourtage = "y";
    utag_data.geo_bg = "gießen";
    utag_data.query_courtage = "y";
    utag_data.ga_cd_cxp_resultview = "listview";
    utag_data.query_timestamp = "11.2023";
    utag_data.KVregio1 = "hessen";
    utag_data.geo_krs = "gießen_kreis";
    
  </script>

  <script>
    function superbannerDefaultSavedSearchForAdvertisement() {
      var savedSearchLink = document.getElementById("saveSearchLinkForAdvertisement").href;
      location.href = savedSearchLink.replace("textlink", "defaultSuperbanner");
    }
  </script>

  <script>
    function getBillboardStore() {
      var billboardStore;

      if (window.IS24 && IS24.resultList && IS24.resultList.reactApp && IS24.resultList.reactApp.BillboardStore) {
        billboardStore = IS24.resultList.reactApp.BillboardStore.getInstance();
      }

      return billboardStore;
    }

    function memorizeFirstLoadedBillboardSize(adLoadedEvent) {
      var billboardStore = getBillboardStore();

      if (!billboardStore || !adLoadedEvent || !adLoadedEvent.size) {
        return;
      }

      if (!billboardStore.getMemorizedPlacementSize()) {
        billboardStore.setMemorizedPlacementSize(adLoadedEvent.size);
      }
    }

    document.addEventListener("ad-slot-loaded", function(event) {
      if (
        event.target.adSlot.adUnitPath === "/4467/IS24_DE/resultlist/banner_top/living" ||
        event.target.adSlot.adUnitPath === "/4467/IS24_DE/resultlist/map_banner_top/living"
      ) {
        memorizeFirstLoadedBillboardSize(event.target.adSlot.deliveredAdData);
      }
    });

    window.S24_OSA = window.S24_OSA || {};
    window.S24_OSA.config = {
      requiredAsyncLoadedMiddlewares: [
        "apsMiddleware",
        "prebidMiddleware"
      ],
      adUnitPathSuffix: "/living"
    };
  </script>

  <s24-ad-targeting style="display:none;">
    {"obj_regio1": "Hessen", "obj_yearConstructedRange": "1,2,3,4,5,6,7,8,9", "obj_noRoomsRange": "2,3,4,5", "obj_ityp": "0", "geo_land": "Deutschland", "obj_baseRentRange": "1,2,3,4,5,6,7,8,9", "obj_regio4": "Innenstadt", "obj_regio3": "Gießen", "obj_livingSpaceRange": "1,2,3,4,5,6,7,8,9,10", "obj_regio2": "Gießen_Kreis", "obj_radius": "5.0"}
  </s24-ad-targeting>


  <div id="save-search" data-save-search-id="" data-entered-from=""></div>

  














<script src="https://www.static-immobilienscout24.de/fro/jquery/3.6.2/jquery.min.js"></script>
<script src="https://www.static-immobilienscout24.de/fro/core/5.3.0/js/core.min.js"></script>


  <script src="https://www.static-immobilienscout24.de/fro/is24/errorhandler/1.2.0/errorhandler.min.js"></script>






    <script src="//tracking.immobilienscout24.de/tr.js?cP--svc_module_name=resultlist&amp;cP--countername=is24.de.finden.wohnen.wohnung_miete.result&amp;addOnClick&amp;reportEventsIndividually"></script><iframe name="__tcfapiLocator" style="display: none;"></iframe>


<script>
  (function mockTrackingIfNotAvailable() {
    var errorMessage = "IS24.TEALIUM is not available. Going over to mock reporting functions.";

    function noop() {
      return;
    }

    if (!IS24.TEALIUM) {
      if (window.console && window.console.warn) {
        window.console.warn(errorMessage)
      }

      IS24.TEALIUM = {
        tracking: {
          report: noop
        },
        cookie: {
          readCookie: noop,
          deleteCookie: noop,
          getCookieAsJson: noop,
          calculateDomain: noop,
          getEventsFromCookieAsArray: noop
        }
      };
    }
  }());
</script>

<script src="https://www.static-immobilienscout24.de/fro/react/16.14.0/react.production.min.js"></script>
<script src="https://www.static-immobilienscout24.de/fro/react-dom/16.14.0/react-dom.production.min.js"></script>
<script src="https://www.static-immobilienscout24.de/fro/mobx/4.15.7/mobx.umd.min.js"></script>
<script src="https://www.static-immobilienscout24.de/fro/mobx-react-lite/2.x/mobxreactlite-2.2.2.umd.production.min.js"></script>
<script src="https://www.static-immobilienscout24.de/fro/mobx-react/6.x/mobxreact-6.3.1.umd.production.min.js"></script>
<script src="https://www.static-immobilienscout24.de/fro/jquery-ui-autocomplete/1.12.1/jquery-ui-autocomplete.min.js"></script>


<script src="https://www.static-immobilienscout24.de/fro/gac/4.0.10/gac.min.js"></script>
<script src="/Suche/resources/build/vendor.js?v=a3228c2cf2d764efdcc5"></script>
<script src="/Suche/resources/build/resultlist.js?v=7a584c40262ee1cc9ace"></script>
<script src="/Suche/resources/build/reactApp.js?v=0bb09b7d05523a953cae"></script><div id="device-state-dummy-palm" class="palm-hide"></div><div id="device-state-dummy-lap" class="lap-hide"></div><div id="device-state-dummy-desk" class="desk-hide"></div>


  <script async="" src="https://osa.s24-media.immobilienscout24.de/aps-is24-resultlist-LATEST.js"></script>
  <script async="" src="https://osa.s24-media.immobilienscout24.de/prebid-is24-resultlist-LATEST.js"></script>
  <script async="" src="https://osa.s24-media.immobilienscout24.de/osa-LATEST.js"></script>










  <script>
    var linkData = {
      data: {
        source: 'resultlist',
        query: JSON.parse(IS24.resultList.resultListModel.searchResponseModel.additional.queryModel).query,
        '$deeplink_android': "is24://retargetStartSearch/radius?realestatetype=apartmentrent&centerofsearchaddress=Gie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;&numberofrooms=2.0-&price=0-800.0&pagesize=20&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0&pagenumber=1&referrer=smartbanner",
        '$deeplink_ios': "is24://retargetShowSearchForm/radius?realestatetype=apartmentrent&centerofsearchaddress=Gie%25C3%259Fen%2520(Kreis);;;1276007006005;;Gie%25C3%259Fen;&numberofrooms=2.0-&price=0-800.0&pagesize=20&pricetype=rentpermonth&geocoordinates=50.58383;8.67789;5.0&pagenumber=1&referrer=smartbanner"
      }
    };

    window.utag_data.branchio_linkdata = linkData;
  </script>







  <script type="text/javascript" src="/assets/immo-1-17" async=""></script>



  <script type="text/javascript">
    window.IS24 = window.IS24 || {};
    IS24.webMetrics = {
      test: "",
      page: "search-web"
    };
  </script>
  <script type="text/javascript" src="https://www.static-immobilienscout24.de/web-metrics/main.js" async=""></script>


  
  
<script>
  (function () {
    function check_webp_feature(feature, callback) {
      var kTestImages = {
        lossy: "UklGRiIAAABXRUJQVlA4IBYAAAAwAQCdASoBAAEADsD+JaQAA3AAAAAA",
        lossless: "UklGRhoAAABXRUJQVlA4TA0AAAAvAAAAEAcQERGIiP4HAA==",
        alpha: "UklGRkoAAABXRUJQVlA4WAoAAAAQAAAAAAAAAAAAQUxQSAwAAAARBxAR/Q9ERP8DAABWUDggGAAAABQBAJ0BKgEAAQAAAP4AAA3AAP7mtQAAAA==",
        animation: "UklGRlIAAABXRUJQVlA4WAoAAAASAAAAAAAAAAAAQU5JTQYAAAD/////AABBTk1GJgAAAAAAAAAAAAAAAAAAAGQAAABWUDhMDQAAAC8AAAAQBxAREYiI/gcA"
      };
      var img = new Image();
      img.onload = function () {
        var result = (img.width > 0) && (img.height > 0);
        callback(feature, result);
      };
      img.onerror = function () {
        callback(feature, false);
      };
      img.src = "data:image/webp;base64," + kTestImages[feature];
    }

    check_webp_feature('lossy', function(featureName, result) {
      document.body.setAttribute('data-usewebp', result ? 'true' : 'false');
    });
  }());
</script>



"""

soup = Soup()
soup.set_soup(text=test2)
print(soup.get_listing())
# x = soup.get_listing()[1]
# print(x.find("a", class_="result-list-entry__brand-title-container").find("h2").get_text())  # tag
# print(x.find("button", class_="result-list-entry__map-link").get_text())  # addresse
# y = x.find_all("dd", class_="font-highlight")  # Todo preis in euro muss gestrippt werden!
# for l in y:
#     print(l.get_text())  # 3 Zi.3 zu 3
# # print(x.find("span", class_= "onlyLarge").get_text()) #Zimmer
#
# print(x.find("div", "margin-right-xs").get_text())
