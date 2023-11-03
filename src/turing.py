from .transition import Transition


class Turing:
    '''
    A class representing a Turing machine.
    '''

    def __init__(self, crudeConfig: dict) -> None:
        '''
        Initialize the Turing machine with a crude configuration

        Args:
            crudeConfig (dict): A dictionary containing the configuration information
        '''
        self.__transformConfig(crudeConfig)

    def __transformConfig(self, crudeConfig: dict) -> None:
        '''
        Transform the crude configuration information into a more usable format

        Args:
            crudeConfig (dict): A dictionary containing the configuration information
        '''
        qStates = crudeConfig['q_states']
        self.qList: list[str] = qStates['q_list']
        self.start: str = qStates['initial']
        self.final: str = qStates['final']

        self.alphabet: list[str] = crudeConfig['alphabet']
        self.tapeAlphabet: list[str] = crudeConfig['tape_alphabet']

        self.simulationStrings: list[str] = crudeConfig['simulation_strings']

        delta: list = crudeConfig['delta']
        self.deltaTuples: list[Transition] = []

        for item in delta:
            params = item['params']
            output = item['output']

            self.deltaTuples.append(Transition(
                params['initial_state'],
                params['mem_cache_value'],
                params['tape_input'],
                output['final_state'],
                output['mem_cache_value'],
                output['tape_output'],
                output['tape_displacement']
            ))

    def __findTransition(self, compareTuple: tuple[str]) -> Transition:
        '''
        Find the transition that matches the given parameters

        Args:
            compareTuple (tuple[str]): The parameters to compare against

        Returns:
            Transition: The transition that matches the given parameters
        '''

        for transition in self.deltaTuples:
            if transition == compareTuple:
                return transition
        return None

    def __currentStep(self, transition: str, injectedString: str) -> str:
        '''
        Get the current step of the simulation

        Args:
            stringList (list[str]): The list of characters in the string
            transition (Transition): The transition to use
            index (int): The index of the current character

        Returns:
            tuple[str]: The parameters of the current step
        '''
        return f'{transition}\t\t\t|- {injectedString}'

    def __insertSymbol(self, stringList: list[str], index: int, transition: Transition) -> None:
        '''
        Insert a symbol into the string list

        Args:
            stringList (list[str]): The list of characters in the string
            index (int): The index of the current character
            symbol (str): The symbol to insert
        '''
        stringListCopy = ['_' if item is None else item for item in stringList]
        stringListCopy.insert(
            index, f'[{transition.initialState}, {transition.initialMemCacheValue}]')
        return ''.join(stringListCopy)

    def __simulate(self, string: str) -> None:
        '''
        Simulate a string on the Turing machine

        Args:
            string (str): The string to simulate
        '''
        pointer = 0
        stringEach = list(string)
        searchTuple = (self.start, string[pointer])
        currentTransition: Transition = self.__findTransition(searchTuple)

        if currentTransition is None:
            print(f'No transition found for {searchTuple}')
            return
        print(self.__insertSymbol(stringEach, pointer, currentTransition))

        toPrintTransition = str(currentTransition)

        isFinal = False
        while True:
            stringEach[pointer] = currentTransition.tapeOutput

            # Handling edge cases when tape is at the end or at the beginning
            pointer += currentTransition.tapeDisplacement
            if pointer < 0:
                pointer = 0
                stringEach.insert(0, None)
            elif pointer >= len(stringEach):
                pointer = len(stringEach)
                stringEach.append(None)

            searchTuple = (currentTransition.finalState,
                           currentTransition.finalMemCacheValue, stringEach[pointer])

            if not isFinal:
                currentTransition = self.__findTransition(searchTuple)
                if currentTransition is None:
                    print(f'No transition found for {searchTuple}')
                    return

            print(self.__currentStep(toPrintTransition,
                                     self.__insertSymbol(stringEach, pointer, currentTransition)))
            toPrintTransition = str(currentTransition)

            # Here will go handling final state
            if isFinal:
                print('Final state reached')
                stringListCopy = [
                    '_' if item is None else item for item in stringEach]
                print(''.join(stringListCopy))
                return

            if self.final == currentTransition.finalState:
                isFinal = True

    def goSimulation(self, num: int = None) -> None:
        '''
        Run the simulation

        Args:
            num (int, optional): The number of the string to simulate. Defaults to None.
        '''
        if num is not None:
            self.__simulate(self.simulationStrings[num])
            return

        for string in self.simulationStrings:
            self.__simulate(string)
            print('-'*100)
