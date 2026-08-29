---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-002-2-tasep-corner-growth-model-and-exponential-dlpp
section_title: "TASEP, corner growth model, and exponential DLPP"
section_number: 2
pages: 2-4
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
This section discusses one of the most well-studied examples of one-dimensional interacting particle systems,
1+1 random growth, and two-dimensional directed polymers.
2.1
TASEP
The totally asymmetric simple exclusion process (TASEP), introduced by Spitzer [82] in 1970, is a continuous-
time Markov process on Z. At any given time, each integer site of Z is occupied by at most one particle.
A particle moves to the adjacent site to its right after a random waiting time, but only if it is empty. The
waiting time is exponentially distributed of mean 1, and the clock starts once the neighboring site becomes
vacant. All waiting times are independent of each other. Note that all moves are to the right (hence, totally
asymmetric), particles can move only one step at a time (simple), and no two particles occupy the same site
at the same time (exclusion). Figure 1 is an example of the conﬁguration at a particular time. Black dots
denote particles, and white dots mark empty sites. In this conﬁguration, only three particles can move, and
they do so independently of each other.
The TASEP is an example of interacting particle systems. General systems may allow, for example, left
moves in addition to right moves, multi-range moves, or several particles at each site.
One particular initial condition we focus on in this article is the step initial condition that the sites in
Z−∪{0} are occupied, and all sites in Z+ are empty. The leftmost picture in Figure 2 shows the step initial
condition.
2
Figure 2: Corner growth model
(1, 1)
(m, n)
Figure 3: Exponential DLPP
Figure 4: An example of Gt
2.2
Corner growth model
The conﬁguration space for the TASEP is {0, 1}Z where 1 represents the presence of a particle and 0 an
empty site. To each conﬁguration, we can associate a zig-zag graph in R2 as in Figure 2. We assign a particle
to a line segment of length
√
2 and slope −1, and an empty site to a line segment of the same length and
slope 1. Juxtaposing the line segments, we obtain a zig-zag graph as in Figure 2. We call the graph a height
function h : R →R for the conﬁguration of the TASEP, and it is unique up to translations. The leftmost
picture in Figure 2 is a translation of h(x) = |x|, and it corresponds to the step initial condition.
The TASEP induces a stochastic evolution of the height function, h(x, t), in which local valleys (corners)
change to local peaks independently with rate 1. The resulting 1+1 random growth process deﬁned by the
height function is called the corner growth process. See Figure 5 for a simulation.
2.3
Exponential DLPP
Consider the two-dimensional lattice Z2
+. Let (m, n) ∈Z2
+. An up/right (i.e., directed) path from (1, 1)
to (m, n) is a sequence p = (pi)m+n−1
i=1
, where pi ∈Z2
+, p1 = (1, 1), pm+n−1 = (m, n), and pi+1 −pi ∈
{(1, 0), (0, 1)}. The thick lines in Figure 3 are an example of a path in which we connected neighboring
integer sites for visual aid. Let ws, s ∈Z2
+, be a collection of independent random variables. The normalized
free energy of the directed polymer measure, introduced by Huse and Henley [50], is
F(m, n; β) = 1
β log
 X
p
eβE(p)
where E(p) =
m+n−1
X
i=1
wpi,
the sum is over all directed paths p from (1, 1) to (m, n), and β > 0 is the inverse temperature. The zero-
temperature, β = ∞, case is called the directed last passage percolation (DLPP). In this case, the normalized
free energy becomes
L(m, n) = max
p
E(p),
which we call the last passage time, interpreting E(p) as the travel time using path p.
For the case when ws ≥0, the DLPP is related to a random growth model. For t > 0, deﬁne the subset
of R2 by
Gt =
[
s∈St
((0, 1]2 + s)
where St = {(m, n) ∈Z2 : L(m, n) ≤t}
and we set L(m, n) = 0 if m ≤0 or n ≤0. See Figure 4. Since L(m, n) is greater than or equal to both
L(m −1, n) and L(m, n −1), we see that if (m, n) ∈Gt, then both points (m −1, n) and (m, n −1) are in
3
Figure 5: Simulation of the corner growth
model
x
y
Figure 6: y = ¯h(x, t) for a few values of t
Gt. The set Gt grows with time t. If we regard Gt in the ﬁrst quadrant as a stack of boxes, we can add a
new box only at the corners.
A special case is the exponential DLPP in which ws are exponentially distributed with mean 1. In this
case, each corner of Gt grows independently of rate 1, i.e., a unit box can be added to each corner independent
at rate 1. Thus, the boundary of Gt is a rotation of the height function of the corner growth process. More
precisely, for the TASEP with the step initial condition and the exponential DLPP,
h(m −n, t) ≥m + n
if and only if
L(m, n) ≤t.
(2.1)
If the TASEP starts with a diﬀerent initial condition, we need to consider the exponential DLPP on a subset
of Z2, determined by the initial condition.
2.4
