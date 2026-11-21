---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-078-geometric-control-of-mechanical-systems
section_title: "Geometric control of mechanical systems"
section_number: null
pages: 83-84
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Many mechanical systems studied in control theory can be modeled by an ordinary differential equation of the form
[90,239]

X() = folx() + D> uit) £iK(0), (361)

i=1
234 S. Blanes et al. / Physics Reports 470 (2009) 151-238

initialized at x(0) = p. Here x € R¢ represents all the possible states of the system, fj are (real) analytic vector fields and
the function u = (uy, ..., Um) (the controls) is assumed to be integrable with respect to time and taking values in a compact
subset U C R™. The vector field fy is called the drift vector field, whereas f;, i > 1, are referred to as the control vector fields.
When fp = 0, the system (361) is called ‘without drift’, and its analysis is typically easier.

For a given set of controls {u;}, Eq. (361) with initial value x(0) is nothing but a dynamical system, which can be analyzed
and (approximately) solved by standard techniques. In control theory, however, one is interested typically in the inverse
problem: given a target x(T), find controls {u;} that steer from x(0) to x(T) [90], perhaps by following a prescribed path. Just
to illustrate these abstract considerations, a typical problem could be the determination of a set of controls that drive the
actions of a robot during a task.

The first step is to guarantee that there exists a solution. This is the problem of controllability. To characterize the
controllability of linear systems of the form

x(t) = A(t)x(t) + B(t)u(t) (362)

is arelatively simple task thanks to an algebraic criterion known as the Kalman rank condition [239,240]. This issue, however,
is much more involved for the nonlinear system (361) [90].

The interest of ME in control theory, as has been already discussed in Section 3.5, stems from the approximate ansatz it
provides connecting the states x(0) and x(T). Thus, the Magnus expansion can be used either to predict a state x(T) fora
given control u or to find reasonable controls u which made reachable, the target x(T) from x(0). Of course, many sets of
controls may exist and it raises questions concerning the cost of every scheme, and consequently the search for the optimal
choice. For instance, the ME has been used in non-holonomic motion planning of systems without drift [241,242]. Among
non-holonomic systems there are free-floating robots, mobile robots and underwater vehicles [242,243].

In the particular case of linear quadratic optimal control problems (appearing in engineering problems as well as in differ-
ential games) a given cost functional has to achieve a minimum. When this happens, Eq. (362) can be written as [244,194] is

x’ = M(t, K(t))x, (363)

where K(t) € R¢*4 has to solve a Riccati differential equation similar to (338) with final condition K(T) = Ky. In other
words, the Riccati equation has to be integrated backward in time, and then to use it as an input in (363). As mentioned, the
Riccati differential matrix equation has received much attention [191,194-196,244-246], but an efficient implementation
to this problem requires further investigation, and methods from ME can play an important role.
