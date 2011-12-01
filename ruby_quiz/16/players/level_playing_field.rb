class LevelPlayingField < Player
  def initialize(opponent)
    # prevent cheater from winning by waiting to pick a strategy
    self.class.class_eval do
      def choose
        [:rock, :paper, :scissors].shuffle.first
      end
    end
  end
end
