from agent import *


def test_agent():
    """Function for testing the agent module"""
    print("Here is the agent module checker")
    print("#===#===#===#===#===#===#===#===#")

    agent = Agent()
    agent.add_property()
    print()
    agent.add_property()
    print()
    agent.add_property()
    print()
    agent.remove_property()
    print()
    agent.display_properties()
    print()
    agent.change_workplace()

if __name__ == "__main__":
    test_agent()