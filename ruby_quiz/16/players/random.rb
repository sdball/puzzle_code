class RandomPlayer < Player
  def choose
    [:rock, :paper, :scissors].shuffle.first
  end

end
