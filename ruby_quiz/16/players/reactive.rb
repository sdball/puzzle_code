class Reactive < Player
  MOVE_THAT_BEATS = {
    rock: :paper,
    paper: :scissors,
    scissors: :rock
  }

  def initialize(opponent)
    @my_move = :paper
  end

  def choose
    @my_move
  end

  def result(my_move, opponent_move, outcome)
    @my_move = MOVE_THAT_BEATS[opponent_move]
  end

end
