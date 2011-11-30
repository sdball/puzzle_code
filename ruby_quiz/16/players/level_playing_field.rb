class LevelPlayingField < Player
  def initialize(opponent)
    # prevent cheater from winning by waiting to pick a strategy
    (class << self; self; end).class_eval do
      def choose
        [:rock, :paper, :scissors].shuffle.first
      end
    end
  end
end
