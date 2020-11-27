# Introduction

For this project different testing approaches where pursued. Core Testing method for The swanclothing was manual testing and user testing. Additionally Testcases based on Django TestCase where introduced to this project to support the development process. In addition to testing the code ran through specific validation services to spot any irregularities or syntax errors. On top of that the project was posted to Code Institutes private #peer-code-review Slack Group to gather some more feedback from students and alumnis. The following documentation provides an detailed overview of the defined testcases, the automatic testing setup, validation service results and insights to challenging bugs that were encoutered during the development of this project.

# Table of Content

- [Introduction](#introduction)
- [Table of Content](#table-of-content)
- [Manual Test Cycles](#manual-test-cycles)
  * [1. Test Navbar](#1-test-navbar)
  * [2. Landing Page](#3-landing-page)
  * [3. Shop](#6-shop)
  * [4. Highlights](#7-highlights)
  * [5. Cart](#8-cart)
  * [6. Checkout](#9-checkout)
  * [7. Sign Up:](#10-sign-up-)
  * [8. Registered Users: Useraccount](#11-registered-users--useraccount)
  * [9. Registered Users: Wishlist](#registered-users--wishlist)
  * [10. Store Management:](#12-store-management-)
- [User Testing](#user-testing)
- [Automatic Tests & Continious Integration](#automatic-tests---continious-integration)
- [Validation Services](#validation-services)
  * [Validation Tools](#validation-tools)
  * [Responsiveness & Rendering](#responsiveness---rendering)
  * [Browser Compatibility](#browser-compatibility)
- [Peer-Code-Review](#peer-code-review)
- [Bug-Log from Development](#bug-log-from-development)



# Manual Test Cycles

## 1. Test Navbar :white_check_mark:

### General Functionalities :white_check_mark:

1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Click every nav item

### Logged in and non-lhttps://tobaskid-swanclothing.herokuapp.com/ions :white_check_mark:

1. Open Browser
2. Open [Swan Clohting](https://tobaskid-swanclothing.herokuapp.com/)
3. Check if navbar contains  
   Shop  
    All productshttps://tobaskid-swanclothing.herokuapp.com/
   Clothing
   Homewear
   Userprofile-icon  
   Cart-icon  
   Search-icon 
   special offer
4. Click Userprofile-icon and login with 
5. Check that navbar icons changed and the follow are present  
   Useraccount-icon  
   Wishlist-icon  
   Cart-icon  
   Search-icon  

### Searchbar opens below nav when search icon is clicked :white_check_mark:

1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Click Search-icon
5. Searchbar should open

### Fixed to top and transparent :white_check_mark:

1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Don't scroll check that nav is transparent

### Changes background and font color on scroll  :white_check_mark:

1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Scroll and check that nav background changes to white and font to black

### Changes background and font color if collapsed on small screens :white_check_mark:

1. Open Browser on medium screen
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Don't scroll
4. Click collapse button
5. Check that nav background changes to white and font to black


## 2. Landing Page :white_check_mark

1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Check that    
   Product details can be accessed by clicking the SHOP Button 





### Shop Categories :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Check that products are displayed and the page title shows the Category

### Shop Productline :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Check that only productline items are displayed and the page title shows the Category & Productline

### Shop All Products
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click All Product
5. Check that matching products are displayed next to eachother.

### Sort Products (3 :white_check_mark: / 1 :beetle:)
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Toggle the Sort switch through all options and check that sorting works accordingly  
    ...Featured Products :white_check_mark:  
    ...Price :beetle:  
    ...Color :white_check_mark:  
    ...Name :white_check_mark:  

    Finding: Sorting by Price works. However due to the datamodel holding an attribut discount_price and normal price the sorting does not take discount_prices into consideration. This should be fixed by either adjusting the model or finding a way to handle it via a function on the get request.

### Check Product types :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Check different card design for regular, sale(red) and pre-order(blue) items

### Non-logged-in user: Get Product Details :white_check_mark:
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. New page should open
7. Page should contain  
   Product image  
   Descripton  
   Size Options
   Add to Cart Button  
   Material information  
   Return & Delivery Information

### Logged-in-user: Get Product Details :white_check_mark:
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Login 
4. Click on shop
5. Click  - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Heart below Add to Cart-Button should be visible

## 4. Highlights :white_check_mark:

### Get Highlights :white_check_mark:
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on HIGHLIGHTS
4. Only one Product 

## 5. Cart :white_check_mark:

### Check empty Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing ](https://tobaskid-swanclothing.herokuapp.com)
3. Click on Cart-Icon
4. Side Drawer Cart shop
5. Placeholder "Nothing in Cart" should be displayed 

### Add item to Cart :white_check_mark:
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click - 
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Chosen Product should be inside the cart view

### Open Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click 
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Fullpage Cart should open

### Add two items to Cart and check Position
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Continue shopping by clicking on the grey overlay or on to the Close button in the top right
9. Cart should Close
10. Choose another product
11. Add Item to Cart
12. Side Drawer Cart should and last added item should be on top

### Checkout from Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click - all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press Checkout Button
9. Checkout Page should open

### Checkout from Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing ](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Fullpage Cart should open
10. Press Checkout Button
11. Checkout Page should open

### Increase Quantity in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click  all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "+" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Quantity should be increased by 1

### Decrease Quantity in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "-" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Quantity should be decreased by 1

### Remove Item(s) in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing ](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click Kids - all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "x" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Product should be removed from Cart

### Increase Quantity in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click Kids - all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "+" Button
11. Page should be reloaded and quantity increased by one

### Decrease Quantity in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "-" Button
11. Page should be reloaded and quantity decreased by one

### Remove Item(s) in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Click on SHOP
4. Click all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "x" Button
11. Page should be reloaded and item should be removed from cart

## 6. Checkout :white_check_mark:

### Checkout AnonymousUser :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Click on SHOP
4. Click  - all products,homewear,clothing,special offer
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click Checkout-Button
9. Should be redirected to checkout page
10. Form for address details & Order Summary should be displayed
11. Fill in form & use test credit card (4242 4242 4242 4242)
12. Submit order
13. Load.
14. Checkout success page should be shown

### Checkout registered user :white_check_mark:

1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com/)
3. Click on SHOP
4. Choose any product by clicking the image
5. Add Item to Cart
6. Side Drawer Cart should open
7. Click Checkout-Button
8. Should be redirected to checkout page
9. Form for address details should be prefilled & Order Summary should be displayed
10. add test credit card (4242 4242 4242 4242)
11. Submit order
12. Loading
13. Checkout success page should be shown

## 7. Sign Up :white_check_mark:

### Sign Up :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click Userprofile-icon
4. Choose Sign Up
5. Fill out the Form
6. Check if confirmation mail was received
7. Confirm email
8. Login with credentials

## 8. Registered Users: Useraccount :white_check_mark:

1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on UserAccount-icon
5. Should see Form 
6. Should see Order History

## Registered Users: Wishlist :white_check_mark:

### Show empty wishlist :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on shop now
5. Should show empty wishlist

### Add product to wishlist :white_check_mark:
1. Open Browser
2. Open [Swan clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Login with 
4. Click on SHOP
5. Choose any product by clicking the image
6. Click Heart below Add to Cart-Button
7. Heart should change from outline to filled

### Show wishlist :white_check_mark:
1. Open Browser
2. Open [Swan Clothing](https://tobaskid-swanclothing.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on Heart-icon
5. Should show wishlist with one liked item

## 9. Store Management :white_check_mark:

### Product Management :white_check_mark:

#### Create Product :white_check_mark:
#### Read Product :white_check_mark:
#### Update Product :white_check_mark:
#### Delete Product :white_check_mark:

### Order Management :white_check_mark:

#### Create Order :white_check_mark:
#### Read Order :white_check_mark:
#### Update Order :white_check_mark:
#### Delete Order :white_check_mark:

### Blog Management :white_check_mark:

#### Create Post :white_check_mark:
#### Read Post :white_check_mark:
#### Update Post :white_check_mark:
#### Delete Post :white_check_mark:

# User Testing

Besides running through the extensive test cycles documented above the URL from the Heroku deployment was shared with friends and family. The following feedback was collected:

- "Great products"
- "Beautiful design"

Following Improvements/Features/Bugs were identified:
* Feature Requests  
  * Feature request: I wish i could include footer in this project.


Build Status:


# Validation Services

## Validation Tools
### [W3C Markup Validation Service](https://validator.w3.org)
## Responsiveness & Rendering
The site was created with the mobile first approach in mind. The following devices / device sizes were used for testing the responsiveness:
* iPhone 11 Pro 
* iPad 10,2"
* MacBook Pro 13"

## Browser Compatibility
The site was tested on the following Browsers:
* [Apple Safari](https://www.apple.com/safari/) 
* [Google Chrome](https://www.google.com/chrome/)
* [Brave Broser](https://brave.com/)
* [Microsoft Edge](https://www.microsoft.com/edge)

On all browsers full site compatibility was identified based on the test cases.

# Peer-Code-Review

The project was peer-reviewed by students from code institute. Feedback was given on the readme files and the code. 

# Bug-Log from Development

The following bugs were identified and mainly fixed during development:
1. Updating userprofile even if checkbox is unchecked on Checkout form:  

   This issue was identified during the extensive testing protocoll and took a while to solve. The problem was that the used JavaScript call to check if the checkbox is checked or unchecked always returned true. Furthermore, the python code didn't identify the javascript `true`/`false` response as `True` or `False`. Therefore the functions did not process the given information as intended. The following lines were introduce to make the function work as intended:
   ```
   stripe_elements.js
   var saveInfo = $('#id-save-info').is(':checked');
   ```
   ```
   webhook_handler.py
   if save_info == "true":
   ```
2. Webhooks for orders  without the optional streetaddressline2 filled out were failing. Therefore customers who didn't provide a line2 street address were not receiving their order confirmation. The problem laid in the model definition. By allowing `null` to be `true` on `street_address2` the webhooks were processed without problems.
3. Adding products to a wishlist if no item was added before on a fresh user failed in the beginning. The solution was to use the `get_or_create` method and check if the object was created or already existed.  
4. Product images were not displayed when using the `{{MEDIA_URL}}` template tag. This was solved by extensivly checking the settings.py and by realizing that the ```django.template.context_processors.media``` was missing in the templates setup. 
5. Importing fixtures to postgres db led to some troubles. This was solved by making sure the charfields are set correct and that especially on long descriptions it makes sense to use TextField.

