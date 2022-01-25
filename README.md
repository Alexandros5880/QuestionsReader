## *Helper Tool For Reading*
###### by Alexandros Platanios

#### Excecution:

* Excecution:
    
        read [-h] -f FILE [-s SPLITCHARACTER] [-a]
        or
        ./read [-h] -f FILE [-s SPLITCHARACTER] [-a]

* Required arguments:
    
        -f FILE, --file FILE  Enter the file.

* Optional arguments:

        -s SPLITCHARACTER, --split SPLITCHARACTER
                            Enter the split characters of questions
        -a, --answer          Display or not the answer.


#### INSTRUCTIONS:

* Create a file.tx with your Question and Answers.
* On right answer put a * to marked as right answer.
* Separate the answers with a spesial character by default is **&&&**
* Save the file.
* Opem cmd on files directory and excecute the app.
* You can put the path of your app on System Variables


#### COMMAND EXAMPLE:

    1). read -h   -->  HELP
    2). read -f ADVANCED.txt  -->  Ask you the questions and give you a grade.
    3). read -f ADVANCED.txt -a  -->  Show you th answers.
    4). read -f importances.txt -s "&&&"  -->  Give a special characters tha seperates the questions.

#### FILE EXAMPLE:

    1). Assume that we have a <section> element with three <article> elements as 
    children. How can we make the <article> elements full-width and layout them 
    vertically using flexbox model?

    a) section {
        display: flex;
        align-items: vertical;
        justify-content: stretch;
    }

    b) section {
        display: flex;
        flex-flow: column nowrap;
        justify-content: stretch;
    }

    c)* section {
        display: flex;
        flex-flow: column nowrap;
        align-items: stretch;
    }

    d) section {
        display: flex;
        align-items: stretch;
        justify-content: column nowrap;
    }

    &&&

    2). In the context of software object-oriented metrics, which guideline is measured in 
    terms of dependencies between units?

    A) Write Code Once
    B) Keep Architecture Components Balanced
    C)* Separate Concerns in Modules 
    D) Keep Unit Interfaces Small

    &&&

    3) In the context of software object-oriented metrics, WMC refers to:

    A) Write Machine Code
    B) Whole Method Complexity
    C) Waste Method Concern
    D)* Weighted Methods per Class

    &&&

    4) Table purchase has as its foreign key the primary key of table clients. Which of the 
    following actions is allowed when using the default setting of the MySQL server:

    A) Create a purchase for a new client that is not contained in the table clients
    B) Delete a client who has made a purchase from the table clients
    C) Change the value of the primary key of table clients
    D)* Find the purchases that correspond to an existing client

    &&&

    5) _______________ restructures code and improves internal structure and design.

    A) Unit Testing
    B) Requirements analysis
    C) Analysis
    D)* Refactoring

    &&&

    6) _________ is an extension of ____________, where we can also use HTML 
    syntax.

    A)* JSX / JavaScript 
    B) JavaScript / JSX
    C) React / JSX
    D) JavaScript / React

    &&&

    7) One of the activities of static software testing is:

    A) Stress testing
    B)* Code reviews 
    C) Unit testing
    D) Beta testing

    &&&

    8) In databases, a(n) ____________ returns all rows when there is a match in one of 
    the tables.

    A) Inner join
    B)* Full join 
    C) Left join
    D) Right join

    &&&

    9) Which of the following sentences in regards to empathy, as a phase of Design 
    Thinking, is INCORRECT?

    A) A tool to help understand a targeted persona.
    B) A tool to help understand programmers’ needs.
    C) Can carry out new research to fill in gaps regarding user understanding.
    D)* Acts as the centerpiece of a software-centered design process.

    &&&

    10) What are the desirable properties of a set classes in order to write maintainable code?

    A High cohesion, high coupling
    B* High cohesion , low coupling
    C Low cohesion , high coupling
    D Low cohesion, low coupling

    &&&

    11) Under which software development methodology requirements and solutions evolve the collaborative effort of self-organizing
    cross-functional teams?

    A Waterfall
    B Spiral
    C* Agile
    D Prototyping

    &&&

    12) In the context of software object-oriented metrics, which of the following options is INCORRECT?

    A* WMC refers to Whole Method Complexity
    B LCOM refers to Lack of Cohesion of Methods
    C CBO refers to Compling Between Object Classes
    D DIT refers to Deph of inheritance Tree

    &&&

    13) Which of the following roles DOES NOT belong to the Composite pattern?

    A* Subject
    B Component
    C Leaf
    D Composite

    &&&

    14) Which of the following is a phase of the software testing cycle?

    A* Requirement Analisys
    B Time Management
    C Project Planning
    D Software Enhancement

    &&&

    15) What is the correct order that testing is usually performed?

    A* Unit Testing -> Component Testing -> Integration Testing -> System Testing -> Acceptance Testing -> Alpha Testing -> Beta Testing
    B Component Testing -> Unit Testing -> Integration Testing -> System Testing -> Alpha Testing -> Acceptance Testing -> Beta Testing
    C System Testing -> Unit Testing -> Component Testing -> Integration Testing -> Acceptance Testing -> Beta Testing -> Alpha Testing
    D Alpha Testing -> Acceptance Testing -> Unit Testing -> Component Testing -> Integration Testing -> System Testing -> Beta Testing

    &&&

    16) Which of the following sentences, in terms of prototyping, is INCORRECT?

    A* The software designer and implementer can get valuable feedback from users only in the early stages of the project
    B The client and the contractor can compare if the software matches the software specification, according to which the software program is build
    C Prototyiping must be an iterative concept of progress
    D Prototypes can be incomlete versions of the software being developed

    &&&

    17) Select the statement that DOES NOT complete the following statement correctly:
    A 3-tier application...

    A * ...is a peer to peer (P2P) computing model.
    B ...often runs separate tiers on operate physical servers.
    C ...has advantages of scalability, reusability and data integrity.
    D ...needs more effort and has higher complexity.

    &&&

    18) Which of the following statements defines OPTIMIZATION?

    A The process of finding and resolving defects that prevent the correct operation of computer software or a system
    B* The process of modifying a software system to make some aspect of it work more efficiently or use fewer resources
    C A version control system (VCS) that is used for software development
    D A program that translates source code from a high-level programming language to a lower level language

    &&&

    19) Whichof the following statement, in regards to code smells, is INCORRECT?

    A Code smells impact code quality negatively
    B Smells can be classified based on the granularity i.e. imolementation, design, and architecture
    C Metrics helps us identity some of the code smells
    D* All of the detected smells must be refactored irrespective of their context

    &&&

    20) Whichof the following statements, in the context of design patterns, is INCORRECT?

    A Application of design patterns improves design quality
    B Design patterns provide a common vocabulary to developers
    C Design patterns promote best practices to write and maintain code
    D* Application of design patterns always results in performance gain

    &&&

    21) Consider the following statements:

    1.Before the project starts a detailed project plan is developed with perticular phases and deliverables
    2.At the and of every phase , a detailed report on deliverables is written by the project manager
    3.A set of processes is detailed foe software developers and other information-technology (IT) professionals to work collaborativelly
    4.At the and of a Sprint , the team holds two events: the Sprint Review and tha Sprint Retrospective
    5.Each day during a Sprint. the taem holds a Daily Scrum (or stand-up) with specific guidelines

    Which of the following describes an activity used When Scrum methodology is used for software development?

    A 1 and 2
    B 2 and 3
    C 3 and 4
    D* 4 and 5

    &&&

    22) What is the sequence of the operations executed in a cursors' body?

    A* Declare > Open >
    Fetch > Close
    B Open>Declare>
    Fetch>Close
    C Declare>Open>
    Fetch>Truncate
    D Open>Declare>
    Fetch>Truncate

    &&&

    23) Which of the following statements, in regards to indexes,is INCORRECT?

    A One or more indexes can be created on single columns
    B Indexes can be created using once or more columns
    C Practically , indexes are type of tables , which keep primary key or index field and a pointer to each record into the actual table
    D* An index is always useful and improves database performance

    &&&

    24) consider the following statements in regards to application architectures:
    1.Centralized systems are easy to maintain.
    2.Distributed systems have moderate scalability.
    3.Centralized systems are very easy to evolve.
    4.Distributed systems can be developed very fast.
    Which of the statements above are TRUE?

    A 1 and 2
    B 3 and 4
    C* 1 and 3
    D 2 and 4

    &&&

    25) Is it better to use exceptions over returned values? Why or why not?

    A* Yes.Returned values dont convey more information about a crash cause.
    B No.Returned values are more concise and informative
    C No.Returned values need no further handling
    D Yes.Returned values are limited by the return type of the method they belong to

    &&&

    26) Which is the correct sequence of the waterfall software development process?

    A Requirement, design, verification, implementation, maitenance
    B* Requirement, design, implementation, verification, maitenance
    C Requirement, implementation, design, verification, maitenance
    D Requirement, verification, design, implementation, maitenance

    &&&

    27) Whichof the following sentences DOES NOT complete CORRECTLY the  Phase: "As Phase of Design Thinking, Empathy...."

    A ...is a tool to help understand a targeted persona.
    B ...is not a tool to help understand programmers needs.
    C ...can carry out new research to fill in gaps regarding user understanding.
    D* ...is the centerpiece of a software-centered design process.

    &&&