class Reactive < Player
  def initialize(opponent)
    @my_move = :paper
  end

  def choose
    @my_move
  end

  def result(my_move, opponent_move, outcome)
    @my_move = winning_move(opponent_move)
  end

  def winning_move(move)
    case move
    when :rock
      :paper
    when :paper
      :scissors
    when :scissors
      :rock
    end
  end

end
