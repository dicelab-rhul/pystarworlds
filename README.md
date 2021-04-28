# PyStarWorlds

PyStarWorlds is currently a single container implementation of the [GOLEM](https://www.cs.rhul.ac.uk/home/kostas/pubs/debs09.pdf) framework implemented in Python. It rationalises various aspects of GOLEM and simplifies its agent model to support rapid prototyping of practical applications. The current system supports the deployment of multiple agents, that can observe and act in the environment in which they are situated. 

PyStarWorlds is currently in a prototype phase and can be thought of more as a library rather than as a standalone platform. 

### Iterations:

- [GOLEM - Prolog/Java]()
- [StarLite - Java]()
- [PyStarWorlds - Python (current)](https://github.com/dicelab-rhul/pystarworlds)

### Why shift to Python? 

- Great for prototyping, rapid development ecosystem with many useful libraries.
- Dynamic typing provides great advantages to developers using the platform. We have found a strongly typed language difficult to work with when building environments on top of StarLite, particularly when writing environment evolution rules - Java generics were not sufficient!
- The defacto language for machine learning research, part of our goal is to make it easy to develop agents with learning capabilities.
- Potential for future extension - a C/C++ backend means that the system has great potential for an efficient implementation, concurrency etc. 

# Environment

The enviroment uses two key abstractions _ambient_ and _physics_ explained below.

## Ambient

The (current) state of the environment which evolves in time according to the rules of the environment (physics). The implementation of the ambient is specific to the domain and is therefore left to the developer to define. 

## Physics

The physics is a collection of rules that govern the evolution of the environment. Events/actions are processed according to these rules. Notifications enable agent perception via a publish and subscribe mechanism. This mechanism is tied to the agents sensors, events that originate from environmental processes or other agents are received by any agent that subcribe to them.

## Containers * 

The GOLEM framework introduced containers as a mechanism for distributing agent environments, PyStarWorlds currently implements a single container. 

## Concurrency * 

The environment runs on a single thread, the agents cycle (perceive-revise-decide-execute) is treated as atomic and agents proceed serially. 
Concurrency has been supported in previous iterations and is planned for the next major version(s) of PyStarWorlds.



## Agents

PyStarWorlds interleaves environment and agent execution in a round-robin fashion. At each time step each agent runs a <i> perceive-revise-decide-execute</i> cycle returning an actionaccording to a given top level goal, determining the agent’s behaviour. We are exploring behaviour for each agent so that it is conceptualised with teleo-reactive condition action rules of the form:

Goal:{Conditions1 &rarr; Action1, ..., Conditionsn &rarr; Actionn},

where <i>Action</i> is either atomic or a <i>SubGoal</i> specified with further condition action rules. These behaviours are translated as Python methods, checking the current observations and the agent state to pursue the most appropriate agent intention at each time step in a dynamic manner.

<img align="right" src="docs/agent.png">

# Related Projects

- [ICUA](https://github.com/dicelab-rhul/ICUA)
- [Vacuum World](https://github.com/dicelab-rhul/vacuumworld) 
- [pyteleor](https://github.com/BenedictWilkins/pyteleor/tree/master/pyteleor)
