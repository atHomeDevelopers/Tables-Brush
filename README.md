# Discover Tables Brush

Tables Brush is a small, light and easy to use module that allows you to draw tables quickly and efficiently in the terminal.  

Tables Brush contains 3 methods, `center_text`, `classifier` and `draw`.

# Examples

### center_text

Usage example for the `center_text` module  

```Python
from Brush import center_text

# center_text will center the text by distributing a number of spaces pass in parameters

my_text = center_text(text="The Raven and the Fox",spaces=10)

# text : the text to center
# spaces : the number of spaces
```

### classifier

Example of use for the `classifier` module

```Python
from Brush import classifier

# classifier allows to classify the elements of a list starting from an index whose values are numerical

objects = [
    ["PC",500],["Mouse",250],["Keyboard",200]
]

# We will classify the above objects starting from index 1 which represents the cost of each item in order 2 (largest to smallest)

objects = classifier(values=objects,index_for_classification=1,order=2)
```
### draw

Example of use for the `draw` module

```Python
from Brush import draw

# draw is the module that allows us to draw our arrays
items = [
    ["Google",1996,"Larry Page"],["Facebook",2004,"Mark Zuckerberg"],
    ["Instagram",2010, "Kevin Systrom"],["Yahoo!",1994, "Jerry Yang"]
]

tables = draw(headers=["Name", "Year", "Inventor/Owner"],values=items)
for i in tables:
    print(i)
```
