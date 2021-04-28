# PyStarWorlds

PyStarWorlds is currently in a prototype phase. It is the current iteration in a line of work on MAS development platforms.

### Iterations:

- [GOLEM - Prolog]()
- [StarLite - Java]()
- [PyStarWorlds - Python (current)](https://github.com/dicelab-rhul/pystarworlds)

### Why shift to Python? 

- Great for prototyping, rapid development ecosystem with many useful libraries.
- Dynamic typing provides great advantages to developers using the platform. We found a strongly typed language difficult to work with when building environments on top of StarLite, particularly when writing environment evolution rules - Java generics were not sufficient!
- The defacto language for machine learning research, part of our goal is to make it easy to develop agents with learning capabilities.
- Potential for future extension - a C/C++ backend means that the system has great potential for an efficient implementation, concurrency etc. 

# Environment

The enviroment uses two key abstractions _ambient_ and _physics_ explained below.

## Ambient

The (current) state of the environment which evolves in time according to the rules of the environment (physics). The specific implementation of the ambient is left up to the developer for now. In future versions we plan to support concurrent access to any user defined datastructues by default. 

## Physics

The physics is a collection of rules that govern the evolution of the environment. Events/actions are processes according to these rules.

## Containers * 

The GOLEM framework introduced containers as a mechanism for distributing agent environments ... (TODO) 

## Concurrency * 

The environment runs on a single thread, the agents cycle (perceive/think/act) is treated as atomic and agents proceed serially. 
Concurrency has been supported in previous iterations and is planned for the next major version(s) of PyStarWorlds.

## Publish and Subscribe

PyStarWorlds uses a type based publish and subcribe mechanism that is tied to the agents sensors. Events that originate from the environmental processes or other agents are received by any agents that subcribe to them.

## Agents

<img align="right" src="docs/agent.png">

# Related Projects

- [ICUA](https://github.com/dicelab-rhul/ICUA)
- [Vacuum World](https://github.com/dicelab-rhul/vacuumworld) 
- [pyteleor](https://github.com/BenedictWilkins/pyteleor/tree/master/pyteleor)
