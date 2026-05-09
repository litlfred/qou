The hexagon axioms of a :refterm[braided monoidal category]{#braided-monoidal-category} guarantee that
$c_{V,V}$ satisfies the Yang--Baxter equation

$$
  (c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  = 
  (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)
$$

on $V^{\otimes 3}$.  This is exactly the braid relation for adjacent
generators, and the far-commutativity relation
$\sigma_i\sigma_j = \sigma_j\sigma_i$ ($\lvert i-j\rvert \geq 2$) follows
from the naturality of the braiding.  Together these verify the Artin
presentation of $B_n$.
