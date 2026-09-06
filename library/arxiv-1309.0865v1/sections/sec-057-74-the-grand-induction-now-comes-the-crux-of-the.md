---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-057-74-the-grand-induction-now-comes-the-crux-of-the
section_title: "The grand induction. Now comes the crux of the argument, a giant induction"
section_number: 7.4
pages: 73-82
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
on maxwidth to prove Proposition 7.6. This entire section re presents the proof.
74 BEN ELIAS AND GEORDIE WILLIAMSON
Fix a rex w for w. Let Xx denote the set of all possible maps which are valid
constructions ofLLx,e with targetw, but which also have polynomials in any region.
We omitw from the notation Xx because, as noted, the choice of reduced expression
giving the ﬁnal target does not matter, because the canonica l isomorphisms between
Hom spaces modulo lower terms preserve the sets Xx.
FixM ≥ 0 and consider the following two statements:
(LM ) For any x with ℓ(x) ≤ M and any w with ℓ(w) ≤ M, choose a single map
LLx,e for each appropriate sequence e with target w. Then every map Bx → Bw of
maxwidth ≤M is in the left R-span of the LLx,e moduloIw.
(XM ) For any x withℓ(x) ≤M and any w withℓ(w) ≤M, every map Bx →Bw of
maxwidth ≤M is in the k-span ofXx moduloIw.
Obviously (LM ) is stronger than (XM ). Our induction will use (XM ) and (LM −1) to
prove (LM ), and (LM ) to prove (XM +1). The base case is M = 0. A map of maxwidth
0 necessarily hasw = ∅ and is just a polynomial, so both (L0) and (X0) hold. Now we
ﬁx x andw. Any map Bx →Bw will have maxwidth M ≥ℓ(w) andM ≥ℓ(x), and if
the map is inXx then it has maxwidth preciselyM =ℓ(x). Thus the statements (LM )
and (XM ) are vacuous for maps to w whenM < ℓ(w). When proving the inductive
statement for maps tow, there will be two separate cases: M =ℓ(w), which we think
of as the “base case” for w because it does not use induction; and M >ℓ(w).
Suppose thatM =ℓ(w), and consider a graph Bx →Bw. There can be no negative
maps on top of the diagram, because of the maxwidth constrain t, so the diagram
ends with a non-negative map. Unless the diagram is purely ne utral, it ends with a
strictly non-negative map which, by the upside-down versio n of Claim 7.2, implies
that the diagram lies within Iw. Hence we can assume that the diagram is neutral,
andℓ(x) = ℓ(w). Any neutral map must consist only of polynomials and 2m-valent
vertices, so it is a rex move with polynomials, and x is also a rex for w. Such a map
is an element of Xx as desired, when e = (1, 1,..., 1). To show (LM ) we need to
show that any single rex move, with polynomials only in the le ftmost region, will
span morphisms consisting of compositions of all rex moves w ith all polynomials
moduloIw. First we use the polynomial forcing relation (5.2) to move t he polynomi-
als to the leftmost region. This leaves behind terms where st rands in the rex move
are broken, but such terms are in Iw, because they have a strictly negative-positive
decomposition. Now we apply Lemma 7.4 to show that the differ ence between two
rex moves is also in Iw.
Thus we have shown (LM ) and (XM ) for the case when M = ℓ(w). We assume
henceforth thatℓ(w)<M .
(LM −1) and (XM ) = ⇒ (LM ). We need to show that each element ofXx is in the span
of our particular ﬁxed choice of LL maps. Since the width of a map in Xx is precisely
ℓ(x), induction already works unless ℓ(x) = M, which we now assume.
SOERGEL CALCULUS 75
To get from an element of Xx associated to e to our particular choice of LLx,e,
we need to force all polynomials to the left, and change our re x moves (possibly
changing the intermediate rexes wk as well). Let us refer to a rex move in the LL
construction by which φk it appears in, and by whether it appears in the form α or
β in Figure 2. In fact, rex moves of the form β inside φk can be viewed instead as
part of α insideφk−1, so we shall assume that β is always trivial, and the location of
the rex move is speciﬁed by which φk it appears in. With this assumption, wk = ws
k
always.
Suppose that we are building a new light leaves map for some (x, e) expressingw,
using arbitrary choices, but we make a single error. While pe rforming a rex move,
we accidentally insert some map with a strictly negative-positive decomposition. We
call a graph of this form an “ LL map with error” or simply an error term . Polyno-
mial forcing (5.2) implies that the cost of sliding a polynom ial across a rex move is
adding an error term. By inspection, every region in an LL map is separated from
the leftmost region by the reduced expression wk, or a subset thereof, so that we can
assume that all polynomials are on the left, modulo error ter ms.
Lemma 7.4 implies that the difference between two rex moves i s an error (that is,
what would be an error if plugged in to the LL construction). Thus if two construc-
tions ofLL differ only in the choice of rex moves, then the difference be tween theLL
moves is spanned by error terms. Two constructions can also d iffer in their choice
ofwk = ws
k, but this can be accounted for by changing rex moves as well. O ne can
replace the identity of wk with a rex move fg whereg : wk → w′
k andf : w′
k → wk.
Then, viewing g as part of α inφk andf as part of α inφk+1, we can effectively re-
placewk withw′
k. (This still works even when dealing with expressions havin gs on
the right, because we can split the rex move into the parts tha t affects and the parts
that do not.) Hence, two different constructions of the same LL differ by error terms.
Thus to show that a particular choice of LL maps spans them all, we need only show
that that this choice of LL maps spans any error term.
This discussion of error terms is not strictly required for t he proof we give next,
but does say that the difference between LL maps is under control, and is useful for
picturing how one would, by hand, attempt to reduce a diagram into the desired
form. We will use the notion of error terms in the later proofs .
Note that adding an error does not affect the maxwidth of a map . LetF denote the
partially constructed error termLLM −1, after the ﬁrst M − 1 steps have been applied.
NowF is a map of width ≤M − 1, so we may apply induction and replace F with
an LL map of our choice , or with a term having dots on top. By adjusting the rex
moves in φM −1 and φM we assume that whenever F is an LL map, the top of F is
our desired wM −1. Now we apply φM to ﬁnish the construction. We draw the four
possibilities.
76 BEN ELIAS AND GEORDIE WILLIAMSON
LL ??
or
??
or
??
or
αα
φ Mφ M
As noted previously , any error in φM itself yields a map contained in Iw because
some dot pulls to the top, so we can assume φM is error free, and that it has our
desired rex move. If F is a term which has a dot on top, then this dot will pull
throughφM to become a dot on the very top except in a single case: when eM is D0
or D1, and the dot is on the ﬁnal strand.
We have sufﬁcient choice of φM such that the ﬁrst diagram is actually one of our
speciﬁed LL maps! The second diagram is in Iw. For the third and fourth diagrams,
we can reapply induction to F without the dot on the blue strand, thus replacing the
question marks withLL maps of our choice (or with more terms of the second type).
Because the top of F was a reduced expression ending in s, removings from the end
still yields a reduced expression for which s is not in the right descent set. Now the
overall expression is our desired LL map, foreM being U1 or U0 respectively (again,
up to the freedom we have to alter α). □
(LM −1) = ⇒ (XM ). Now let us ﬁx w withℓ(w)< M, and prove that (LM −1) implies
(XM ) for w. Consider a diagram of maxwidth ≤ M. If the maxwidth M is never
attained then we may use induction, so let us assume that widthM is attained at least
once. WidthM may be maintained for a period of time using 2m-valent vertices, and
eventually the width may drop again toM −1 and rise back toM for another interval.
Claim 7.7. Assume (LM −1). A map Bx → Bw with ℓ(x) ≤ M − 1 which only reaches
widthM for one continuous interval is in the span of Xx moduloIw.
Claim 7.8. Assume (LM −1). A map Bx → Bw withℓ(x) = M which only reaches width
M for one continuous interval starting at the bottom is in the s pan ofXx moduloIw.
Suppose that we can show these two claims. Then we may simplif y the diagram
from top to bottom as follows. Consider the ﬁrst interval whe re widthM appears. If
that extends all the way to the bottom of the map, we can use Cla im 7.8 to conclude
thatXM holds. If the interval ends and we return to widthM −1, we can apply Claim
7.7 to replace that region with an LL map (by (LM −1), any LL map we choose), and
thus the whole region now stays below width M − 1. After doing this, the next
interval becomes the ﬁrst interval, and we repeat the argume nt.
We proceed to prove Claim 7.8 ﬁrst. Let η denote the map in question (having
bottomx), y the topmost sequence where width M is attained, and z the sequence
immediately above, havingℓ(z) = M − 1. The map Bz →Bw has maxwidthM − 1 so
by induction we can assume it is any construction of LLz,e we choose. We can ignore
polynomials on the left of the diagram. We begin by treating t he case without 2m-
valent vertices on bottom, wherex =y. There are two cases, to be treated differently .
SOERGEL CALCULUS 77
= LL or LLη
yy
zz
Claim 7.9. Suppose a negative (merging) trivalent is added below a ligh t leaves map. The
result is light leaves.
Proof. Suppose that the new trivalent vertex is attached to the k-th strand, with xk =
s. There are four choices for ek: U0, U1, D0, D1. The composition will be a light
leaves with (ss ) instead of xk and one of four sequences instead of ek: (U1 D1), (U1
D0), (D0 D0) or (D0 D1) respectively . This is pictured below:
U0
=
U1 D1
U1
=
U1 D0
D0
=
D0 D0
D1
=
D0 D1
□
Claim 7.10. Suppose that we add a negative (bottom) dot after the k-th strand of an LLz,e
of our choice, yielding a map from By. The result is in Xy.
Proof. Suppose that the new boundary dot is colored s. If s is not in the right descent
set of wk, then the result is an LL map, with the new strand being U0. If s is in the
right descent set, by choosing our LLz,e appropriately , we can assume thats occurs
on the right of wk. Now the statement follows from the equality below, because both
terms on the RHS are in Xy. We use the decomposition of Remark 6.4, and relation
(5.2). Remember that the use of 1
2 is unnecessary , as any dual basis will do.
LL
LL
1 1 1
=
LL
LL
1 1 1 +
LL
LL
1 1 1
D0 D0
1
2
1
2
□
Remark 7.11. While this is the only use in this chapter of the assumption of Demazure
Surjectivity , it is signiﬁcant. Without this assumption, d ouble leaves will not form a
basis in the simplest counterexample: maps from Bs ⊗Bs →Bs.
Now we want to add more 2m-valent vertices below this LL map. First we prove
a useful inductive lemma.
78 BEN ELIAS AND GEORDIE WILLIAMSON
Claim 7.12. Assume (LM −1), and let ℓ(x) = M. Suppose we have a map Bx →Bw which
never returns to width M after it leaves it. Suppose further that the map splits as fol lows for
some 0<k <M .
??
??
{
<k
k
Then the map is in the span of Xx, moduloIw.
Proof. Both question mark boxes have width strictly less than M, so by induction,
we can assume that these boxes contain LL maps of our choice, or morphisms with
dots on top. The rest of the proof is exactly the same as the pro of in the previous
section. We induct on the width of the sequence v with the dashed line through it.
By an application of Lemma 7.5 we can assume without loss of ge nerality that v is
actually a reduced expression for v ∈W . We write the lower box as fv +fl, wherefv
is a linear combination of light leaves and fl is in Iv, and we write the upper box as
gw,1 +gw,0 +gl wheregl is inIw,gw,1 is a linear combination of light leaves beginning
with all U1 for v, andgw,0 is a linear combination of light leaves which do not begin
with U1’s, meaning that somewhere on v is a U0. In the product, combining fv with
gw,1 will give valid constructions for an element of Xx. Combining anything with gl
will be in Iw. For a term with either fl orgw,0, we draw a new dashed line to avoid
the dot; this decreases the width of the dashed line by one. In duction then ﬁnishes
the proof. □
Claim 7.13. Assume (LM −1), and let ℓ(x) = M. Placing a 2m-valent vertex below a
diagram inXw will result in a diagram in the span of Xx moduloIw.
Proof. Any light leaves map with a neutral map below it is non-positi ve, so that it
will never return to width M after it departs. Suppose that we add the 2m-valent
vertex of colors s,t to strands xl+1 through xl+m of a light leaves map LLx,e. For
any 0 < k ≤ l or l +m ≤ k < M, we can split the diagram into LL≤k and the
remainder as in Remark 6.4, placing the new 2m-valent vertex below whichever half
is appropriate. Therefore, if any such LL≤k maps to a shorter sequence, we can
simply use Claim 7.12 to ﬁnish the proof. This allows us to red uce to the following
special case:x≤l is a reduced expression and e≤l is all U1 (this includes the possibility
l = 0); unlessl+m =M,x≤M −1 is a reduced expression and e≤M −1 is all U1. Any time
where el+1 through el+m are all U1, the 2m-valent vertex can be viewed as part of the
rex move in LLx,e, so the result is clearly in Xx. Hence, we assume that M =l +m,
and (x, e)≤l is a reduced expression for wl ∈W .
Furthermore, we can alter any rex moves in LLx,e at will. The difference term will
have an error. If this error occurs in φk fork < Mthen we can use induction on the
SOERGEL CALCULUS 79
error version of LL≤k, which has width ≤ M − 1, to rewrite it in terms of LL maps
and graphs with dots on top. These can be dealt with in the fami liar manner. If the
error occurs in φM , it produces a dot on top, and is thus in Iw.
Hence, we can choose any desired reduced expression wl forwl. Now wl =uv for
v ∈ Ws,t the dihedral group, and u a minimal right coset representative of Ws,t. We
can choose a rex for wl of the form uv. Now the remaining terms of x are all s ort,
and given any sequence of 1’s and 0’s, the assignment of U and D only depends onv
and not on u. Moreover, the rex moves required to send s ort to the right when a D
appears (i.e. the rex moves of type β in Figure 2) can all be performed within vx>l,
preserving u. Suppose that they are so in LLx,e. Then the reduction to light leaves
form does not depend on u at all. We could assume without loss of generality that
wl =v ∈Ws,t, and the entire diagram only contains 2 colors! Morphism spaces in D
for dihedral groups are already proven in [Elib] to be the rig ht size, which implies
the result; alternatively , one could do a case by case analys is. □
Remark 7.14. The case by case analysis can be quite interesting, although tedious.
The following is a worthwhile exercise. Let m = 3 , and v = sts. Let x = ststst and
e = (U1,U 1,U 1,D 0,D 0,D 0). First draw LLx,e, and then place a 2m-valent vertex
below the D0’s, and transform the diagram into light leaves f ormat for stssts. This
involves repeated applications of (5.6). The exact same cal culation works for general
m.
We have now proven Claim 7.8. In order to prove Claim 7.7, we ne ed only put a
positive generator below a map in Xy forℓ(y) = M.
Claim 7.15. Assume (LM −1). Suppose that ℓ(y) = M and we add a positive (splitting)
trivalent below a map in Xy to obtain a map Bx →Bw. Then the result is in the span of Xx,
moduloIw.
Proof. Suppose that the trivalent vertex is added toyk andyk+1. There are 8 consistent
possibilities for ek and ek+1: ek can be any of U0, U1, D0, D1, and it determines
whether ek+1 is U or D. In fact, if ek is U0 or D1, the result is manifestly in light
leaves format.
U0
=
U1
=
U1
U0
U0
U0
D1
=
D1
U0 D1
=
D0
U1
On the other hand, if ek is U1 or D0, the result locally looks like the following.
80 BEN ELIAS AND GEORDIE WILLIAMSON
U1
D0 or D1
D0 or D1
D0
LL*
*
By “D0 or D1” we mean that the topmost trivalent in these graph s is as pictured
when ek+1 is D0, and has a further dot on top when ek+1 is D1; this extra dot will
not affect our discussion. The dashed line indicates where w idthM is reached. The
asterisk box in these graphs is some rex move between two rexe s which both have s
on the far right.
In fact, we believe both these diagrams to be zero. Let us paus e to state a compu-
tational conjecture.
Conjecture 7.16. For any rex move β : w → w′, where both w and w′ have s on the far
right, one has
(7.1) =
β
β
w′ w′
w w
s
s .
This would imply, using (5.3) and (5.5), that the following is zero.
(7.2) = 0β
Let us continue the proof without assuming this conjecture.
Which rex move appears in the asterisk box? If the rex move doe s not involve the
rightmost s-colored strand, then clearly the result is zero by (5.3) and (5.5). Since
two rex moves are equal modulo lower terms, we may assume that the asterisk box
actually contains a strictly negative map followed by a stri ctly positive map. More-
over, Lemma 7.4 guarantees that both the top and bottom of the asterisk box has a
boundary dot.
We will now use these boundary dots to reduce the maxwidth of t he diagram be-
low M. The bottom dot (resp. top dot) appears either in one of the in itial k − 1
strands, or on the ﬁnal s-colored strand. If the dot appears on the ﬁnal s-colored
strand, then it will pull into the nearby trivalent vertex by (5.4). Otherwise, using
SOERGEL CALCULUS 81
rectilinear isotopy , the dot can be pulled past this trivale nt vertex. After perform-
ing these operations to the top and bottom dots, the resultin g diagram never fac-
tors through a sequence of width M, and therefore (LM −1) implies that it can be
expressed in the span of light leaves. □
Claim 7.17. Assume (LM −1). Suppose that ℓ(y) = M and we add a positive (top) dot below
a map in Xy to obtain a map Bx →Bw. Then the result is in the span of Xx, moduloIw.
Proof. Suppose that the dot is attached to yl inLLy,e. Let us draw a number of possi-
bilities for what can happen to the dot.
U0
= D0
=
U1 U1 D0
= U1
U1 D1
= U0
D1
= = =
α s
JWJW
In the ﬁrst row, el is U0 or D0 and is quickly taken care of. When el is U1, what
happens to the dot next can be a number of things. If the dot hit s a rex move we
end up on the third row, which we will discuss shortly . Otherw ise, we consult the
second row. The dot either makes it all the way to the top (endi ng up inIw) or it runs
into a D0 or D1 and is taken care of. Finally , if el is D1, we end up in the ﬁrst picture
on the third row. The diagram on the right hand side clearly ha s width ≤M − 1, so
it can be taken care of with (LM −1).
We have now proven this result except when the dot meets a rex m ove. We can
induct on the number of 2m-valent vertices in the rex move; the base case has just
been done. Each term in the Jones-Wenzl projector will have a dot on top. We can
resolve that dot by induction to get an LL map with width ≤M − 1. After doing so,
the remainder of the diagram has width ≤M − 1, and we can apply (LM −1) to ﬁnish
the proof. □
Remark 7.18. There is an alternative proof. We can use Claim 7.12 and the sa me style
of argument as in Claim 7.13 to reduce to the case where (y, e)<M −1 is a reduced
expression with all U1’s, and eM is D. Moreover, we can choose whatever rex moves
we desire. Now the case by case analysis is easy , using some of the cases above.
This concludes the proof of Claim 7.7, and consequently of the fact that (LM −1) = ⇒
(XM ). □
82 BEN ELIAS AND GEORDIE WILLIAMSON
