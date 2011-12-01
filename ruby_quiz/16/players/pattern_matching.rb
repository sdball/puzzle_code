class PatternMatching < Player
  MOVE_THAT_BEATS = {
    rock: :paper,
    paper: :scissors,
    scissors: :rock
  }
  def initialize(opponent)
    @first_game = true
    @my_move = :rock
    @patterns = {
      rock: {},
      paper: {},
      scissors: {}
    }
  end

  def choose
    @my_move
  end

  def result(mine, theirs, outcome)
    store_moves(mine, theirs)
    plan_next_move
    @first_game = false
  end

  private
    def store_moves(mine, theirs)
      unless @first_game
        store_pattern(mine, theirs)
      end
      @my_last_move = mine
      @their_last_move = theirs
    end

    def store_pattern(mine, theirs)
      if @patterns[@my_last_move][@their_last_move]
        @patterns[@my_last_move][@their_last_move] << theirs
      else
        @patterns[@my_last_move][@their_last_move] = [theirs]
      end
    end

    def plan_next_move
      @my_move = MOVE_THAT_BEATS[their_likely_next_move] || :rock
    end

    def their_likely_next_move
      their_moves = @patterns[@my_last_move][@their_last_move]
      return [:rock, :paper, :scissors].shuffle.first if their_moves.nil?
      count = Hash.new(0)
      their_moves.each do |move|
        count[move] += 1
      end
      count.sort_by {|key, value| value}.last.first
    end
end
