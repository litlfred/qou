---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-026-7-commands
section_title: "Commands"
section_number: 7
pages: 20-22
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
encourage you to use a Java IDE, like Eclipse, because in my opinion, entering commands in the console of a good IDE is
more convenient than doing the same in the terminal. You are only going to run Walnut inside the IDE and use the IDE’s
console (not the source code editor) to enter Walnut commands. Here is the instructions on how to run Walnut inside Eclipse
for Java:
1. Go to this link and download Eclipse for Java for your speciﬁc platform.
2. Downloaded ﬁle is probably compressed. To start Eclipse, ﬁrst uncompress the ﬁle, then click on the ﬁle named
Eclipse.
3. When you run Eclipse, it asks for a workspace address. Feel free to enter the path to your desired directory.
Now we need to import Walnut into Eclipse as a Java project:
4. When in Eclipse, go to “File > Import ... ”. In the dialog that opens up choose “General > Existing Project into Workspace”.
5. In the dialog that opens up, click browse, ﬁnd Walnut (that you downloaded and uncompressed in the Installation
section) and press open. Then click ﬁnish.
6. Close the Welcome page in your Eclipse window.
7. On the "Project Explorer" (probably) on the left of your screen, you can see only one project (the one that you just
imported). Click on it. Then click on “src”. Then double click on “prover.java”.
8. You will see a green circle with a white triangle inside it. Click on it. This causes Walnut to run.
9. You can enter your Walnut commands in the console window in your Eclipse. If you are not able to ﬁnd the console
window, go to “Window > Show View > Other > General > Console” to open it.
7
Commands
Every command ends in either a colon, double colon, or a semicolon. If you want to see the reports on the intermediate
steps of a computation use colon or double colon, otherwise use semicolon. For example, if we type:
eval
test "a = b +1" :
20
we get an output similar to the following written in the console:
a = b +1:2
states −1ms
total computation time : 2ms
which explains that the automaton for predicate a = b +1 has 2 states and it took 2 milliseconds to compute it. We use blue
to denote predicates. Here we use grey to indicate the output produced by Walnut in the console. We use red to indicate
errors in the console.
Walnut prints to console only the major steps of a computation when a single colon is used to end a command. Use two
colons if you want to see all the steps behind the scene (cross product 4.1, quantiﬁcation 4.2, minimizations, converting
NFAs to DFAs (determinizations), etc.):
eval
test "a = b +1" : :
then we get an output similar to the following written in the console:
computing b +1
computed a +1
computing a = (b +1)
computing &:1
states −2 states
computing cross product :1
states −2 states
computed cross product :2
states −1ms
minimizing :2
states
determinizing :2
states
determinized :2
states −0ms
minimized:2
states −0ms
computed &:2
states −1ms
quantifying :2
states
minimizing :2
states
determinizing :2
states
determinized :2
states −0ms
minimized:2
states −0ms
quantified :2
states −0ms
fixing leading zeros :2
states
determinizing :2
states
determinized :2
states −1ms
minimizing :2
states
determinizing :2
states
determinized :2
states −0ms
minimized:2
states −0ms
fixed leading zeros :2
states −1ms
computed a = (b +1)
a = (b +1):2
states −2ms
total computation time : 34ms
Whitespace is ignored. You can, for example, span one single command into multiple lines to improve readability. So, for
example, you can write the following interchangeably:
eval
test "a = b +1" ;
eval
test
"a = b +1" ;
eval
test "a
= b +1" ;
eval
test
"a = b +1"
;
In case we forget to separate the name test and predicate a = b +1 of the eval command, Walnut catches it by returning
an error:
21
eval
test "a = b +1" :
invalid use of eval /def command
:
eval
test "a = b +1" :
Here is the full list of commands in Walnut and we will go over them one by one in detail:
• exit
• eval <name> <predicate>
• def <name> <predicate>
• macro <name> <template>
• reg <name> <number system> <regular expression>
• reg <name> <alphabet> <regular expression>
• load <ﬁle name>
7.1
