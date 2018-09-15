"""
Veneer
Here at Veneer we strive to provide the best marketplace experience to connect vetted art dealers with premium galleries. Create a marketplace for people and organizations to buy and sell pieces of art!

In this project we'll be developing classes and objects that represent the various responsibilities of art dealership software.

"""

class Art:
  def __init__(self,artist,title,medium,year,owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return "{}. \"{}\". {}, {}. {}. {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self,new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    
  def show_listings(self):
    for i in self.listings:
      print(i)
    
vaneer = Marketplace()
#print(vaneer.show_listings())

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return "{}, {}.".format(self.art.title, self.price)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      vaneer.add_listing(new_listing)
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
    for listing in vaneer.listings:
      if listing.art == artwork:
        art_listing = listing
        break
    if art_listing != None:
      art_listing.art.owner = self
      vaneer.remove_listing(art_listing)

edytta = Client("Edytta Halpirt", "Private Collection", False)    

girl_with_mandolin = Art("Picasso, Pablo",  "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta) 

#print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, "6M  (USD)")
#vaneer.show_listings()

moma = Client("The MOMA", "New York", True)

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)    
vaneer.show_listings()
    
