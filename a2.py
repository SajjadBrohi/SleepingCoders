#!/usr/bin/env python3
"""
Assignment 2 - Sleeping Coders
CSSE1001/7030
Semester 2, 2019
"""

import random

__author__ = "Sajjad Brohi: 45667785"

class Card(object):
    """
    Represents a card in the game
    """
    def play(self, player, game): 
        """
        Removes the card from player's hand and places a new one from
        the pickup pile.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
        """
        player.get_hand().remove_card(player.get_hand().get_cards().index(self))
        player.get_hand().add_cards(game.get_pickup_pile().pick())
        game.set_action('NO_ACTION')
        
    def action(self, player, game, slot):
        """
        Returns None as this method is used only on a special card

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
            slot (int): Represents the index number of the card
        """
        return None
    
    def __str__(self):
        """
        Represents the Card in a string format
        """
        return f'Card()'
    
    def __repr__(self):
        """
        Represents the Card in a string format
        """
        return f'Card()'

        
class NumberCard(Card):
    """
    Represents a NumberCard in the game
    """
    def __init__(self, number):
        """
        Constructs a NumberCard from a provided number

        Parameters:
            number (int): Represents the number of the NumberCard
        """
        self._number = number
        
    def play(self, player, game):
        """
        Removes the card from player's hand and places a new one from
        the pickup pile. Also, moves the game to the next player.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
        """
        super().play(player,game)
        game.next_player()
        
    def get_number(self):
        """
        Returns the number of the NumberCard
        """
        return self._number
    
    def __str__(self):
        """
        Represents the NumberCard in a string format
        """
        return f'NumberCard({self._number})'

    def __repr__(self):
        """
        Represents the NumberCard in a string format
        """
        return f'NumberCard({self._number})'


class CoderCard(Card):
    """
    Represents a CoderCard in the game
    """
    def __init__(self, name):
        """
        Constructs a CoderCard from a provided name

        Parameters:
            name (str): Represents the name of the CoderCard
        """
        self._name = name
        
    def get_name(self):
        """
        Returns the name of the CoderCard
        """
        return self._name
    
    def play(self, player, game):
        """
        Sets the action status of the game to a state of no action
        being performed.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
        """
        game.set_action('NO_ACTION')
        
    def __str__(self):
        """
        Represents the CoderCard in a string format
        """
        return f'CoderCard({self._name})'
    
    def __repr__(self):
        """
        Represents the CoderCard in a string format
        """
        return f'CoderCard({self._name})'
    

class TutorCard(Card):
    """
    Represents a TutorCard in the game
    """
    def __init__(self, name):
        """
        Constructs a TutorCard from a provided name

        Parameters:
            name (str): Represents the name of the TutorCard
        """
        self._name = name
        
    def get_name(self):
        """
        Returns the name of the TutorCard
        """
        return self._name
    
    def play(self, player, game):
        """
        Removes the card from player's hand and places a new one from
        the pickup pile. Also, moves the game to the next player and
        performs the action of picking up a coder.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
        """
        super().play(player,game)        
        game.set_action('PICKUP_CODER')
        
    def action(self, player, game, slot):
        """
        The card is added to the player's deck of coders, the position of said
        card in the sleeping coders' deck is replaced with None. Also, sets the
        action status of the game to a state of no action and moves to next player.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
            slot (int): Represents the index number of the card
        """
        player.get_coders().add_card(game.get_sleeping_coder(slot))
        game.set_sleeping_coder(slot, None)
        game.set_action('NO_ACTION')
        game.next_player()
        
    def __str__(self):
        """
        Represents the TutorCard in a string format
        """
        return f'TutorCard({self._name})'
    
    def __repr__(self):
        """
        Represents the TutorCard in a string format
        """
        return f'TutorCard({self._name})'
    

class KeyboardKidnapperCard(Card):
    """
    Represents a KeyboardKidnapperCard in the game
    """
    def play(self, player, game):
        """
        Removes the card from player's hand and places a new one from
        the pickup pile. Also, moves the game to the next player and
        performs the action of stealing another player's coder.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
        """
        super().play(player,game)
        game.set_action('STEAL_CODER')
        
    def action(self, player, game, slot):
        """
        The card is removed from the target player's deck of coders and
        added to the current player's deck. Also, sets the action status
        of the game to a state of no action and moves to next player.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
            slot (int): Represents the index number of the card
        """
        card = player.get_coders().get_card(slot)
        game.current_player().get_coders().add_card(card)
        player.get_coders().remove_card(slot)
        game.set_action('NO_ACTION')
        game.next_player()
        
    def __str__(self):
        """
        Represents the KeyboardKidnapperCard in a string format
        """
        return 'KeyboardKidnapperCard()'
    
    def __repr__(self):
        """
        Represents the KeyboardKidnapperCard in a string format
        """
        return 'KeyboardKidnapperCard()'

class AllNighterCard(Card):
    """
    Represents an AllNighterCard in the game
    """
    def play(self, player, game):
        """
        Removes the card from player's hand and places a new one from
        the pickup pile. Also, moves the game to the next player and
        performs the action of putting another player's coder to sleep.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
        """
        super().play(player,game)
        game.set_action('SLEEP_CODER')
        
    def action(self, player, game, slot):
        """
        The card is removed from the target player's deck of coders and
        added to the sleeping coders deck. Also, sets the action status
        of the game to a state of no action and moves to next player.

        Parameters:
            player (Player): The player to perform the action on
            game (CodersGame): To access the game of Sleeping Coders
            slot (int): Represents the index number of the card
        """
        for index,card in enumerate(game.get_sleeping_coders()):
            if card == None:
                index_number = index
                break
        card = player.get_coders().get_card(slot)
        game.set_sleeping_coder(index_number,card)
        player.get_coders().remove_card(slot)
        game.set_action('NO_ACTION')
        game.next_player()
        
    def __str__(self):
        """
        Represents the AllNighterCard in a string format
        """
        return 'AllNighterCard()'
    
    def __repr__(self):
        """
        Represents the AllNighterCard in a string format
        """
        return 'AllNighterCard()'
    

class Deck(object):
    """
    Represents a deck in the game
    """
    def __init__(self, starting_cards=None):
        """
        Constructs a Deck with the starting cards as the argument,
        which is None by default.

        Parameters:
            starting_cards (List): Represents the cards in the deck
        """
        if starting_cards == None:
            self._starting_cards = []
        else:
            self._starting_cards = starting_cards

    def get_cards(self):
        """
        Returns the list of starting cards in the deck.
        """
        return self._starting_cards
    
    def get_card(self, slot):
        """
        Returns the card in the given slot of the deck.
        
        Parameters:
            slot (int) : The index of the card that is to be returned.
        """
        return self._starting_cards[slot]
    
    def top(self):
        """
        Returns the card at the end of the deck list.
        """
        return self.get_card(-1)

    def remove_card(self, slot):
        """
        Removes the card in the given slot of the deck.
        
        Parameters:
            slot (int) : The index of the card that is to be removed.
        """
        self._starting_cards.pop(slot)

    def get_amount(self):
        """
        Returns the amount of cards in the deck.
        """
        return len(self.get_cards())

    def shuffle(self):
        """
        Returns a deck with all of its cards randomly shuffled.
        """
        return random.shuffle(self._starting_cards)
    
    def pick(self, amount=1):
        """
        Returns a list of cards picked up from the end of the deck.

        Parameters:
            amount (int) : The amount of cards to pick.
        """
        pick = []
        i = 0
        while i > (-amount):
            pick += [self.get_cards().pop(-1),]
            i -= 1
            
        return pick
    
    def add_card(self, card):
        """
        Returns the deck after adding a card at the end of it.

        Parameters:
            card (str) : The card to add to the deck.
        """
        return self.get_cards().append(card)
    
    def add_cards(self, cards):
        """
        Adds a list of cards at the end of the deck.

        Parameters:
            cards (list) : The list of cards to add.
        """
        self._starting_cards += cards
        
    def copy(self, other_deck):
        """
        Returns the deck after adding all of the cards from
        the given deck.

        Parameters:
            other_deck (Deck) : The deck of cards to copy.
        """
        return self.add_cards(other_deck.get_cards())

    def __str__(self):
        """
        Represents the Deck in a string format
        """
        cards = str(self.get_cards()).strip('[')
        cards = cards.strip(']')
        return f'Deck({cards})'

    def __repr__(self):
        """
        Represents the Deck in a string format
        """
        cards = str(self.get_cards()).strip('[')
        cards = cards.strip(']')
        return f'Deck({cards})'

    
class Player(object):
    """
    Represents a player of the game
    """
    def __init__(self, name):
        """
        Constructs a Player with the name as the argument.

        Parameters:
            name (str): Represents the name of the Player.
        """
        self._name = name
        self._cards = Deck()
        self._coders = Deck()
        
    def get_name(self):
        """
        Returns the name of the player.
        """
        return self._name

    def get_hand(self):
        """
        Returns the player's deck of cards.
        """
        return self._cards
    
    def get_coders(self):
        """
        Returns the player's deck of coder cards.
        """
        return self._coders
    
    def has_won(self):
        """
        Returns True if the length of player's deck of coder cards is
        greater than or equal to 4. Returns False otherwise.
        """
        if len(self.get_coders().get_cards())>=4:
            return True
        return False
    
    def __str__(self):
        """
        Represents the Player in a string format
        """
        return f'Player({self.get_name()}, {self.get_hand()}, {self.get_coders()})'
    
    def __repr__(self):
        """
        Represents the Player in a string format
        """
        return f'Player({self.get_name()}, {self.get_hand()}, {self.get_coders()})'
        
    
def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
