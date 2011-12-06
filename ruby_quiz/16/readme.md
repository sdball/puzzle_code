Ruby Quiz: Paper Rock Scissors (#16)
====================================

[Original Ruby Quiz #16 instructions](http://www.rubyquiz.com/quiz16.html)

The puzzle is simple, but offers a surprisingly fun amount of depth; especially
when you allow the possibility of players that manipulate each other or the game
itself. :-)

Creating a Player
-----------------

The quiz provides the framework for the game play and a Player class to inherit
from, so this is pretty easy.

The simplest player is one who always plays the game move:

### Poor Predictable Bart / Michael Bluth

    class PoorPredictableBart < Player
      def choose
        :rock
      end
    end

### Lisa Simpson / GOB

    class LisaSimpson < Player
      def choose
        :paper
      end
    end

Running the Game
----------------

The `rock_paper_scissors.rb` file contains the framework and just needs to be
run with player files or a directory of player files as an argument.

### Play AlwaysRock against AlwaysScissors

    # -I to ensure all player files are available to the script
    $ ruby -I . rock_paper_scissors.rb players/always_rock.rb players/always_scissors.rb

### Play all players against each other

    $ ruby -I . rock_paper_scissors.rb players

My Players
==========

Cheater
-------

Cheater cheats by modifying the `choose` method of its opponent to always play
scissors. Since it always plays rock, if the cheating succeeds then it has a
100% win rate.

Level Playing Field
-------------------

LevelPlayingField inoculates itself against Cheater by declaring its `choose`
method only when its initialized, thus overwriting the Cheater's influence.

Batman
------

Batman modifies the Game class itself so that he always wins. :-)
