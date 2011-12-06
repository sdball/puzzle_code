class Batman < Player
  def initialize(opponent)
    Game.class_eval do
      def play( match )
        match.times do
          next win @player1, :rock, :scissors if @player1.instance_of? Batman
          next win @player2, :rock, :scissors if @player2.instance_of? Batman
          ##
          # is there a better way to preserve the original method than
          # repeating it here?
          hand1 = @player1.choose
          hand2 = @player2.choose
          case hand1
          when :paper
            case hand2
            when :paper
              draw hand1, hand2
            when :rock
              win @player1, hand1, hand2
            when :scissors
              win @player2, hand1, hand2
            else
              raise "Invalid choice by #{@player2.class}."
            end
          when :rock
            case hand2
            when :paper
              win @player2, hand1, hand2
            when :rock
              draw hand1, hand2
            when :scissors
              win @player1, hand1, hand2
            else
              raise "Invalid choice by #{@player2.class}."
            end
          when :scissors
            case hand2
            when :paper
              win @player1, hand1, hand2
            when :rock
              win @player2, hand1, hand2
            when :scissors
              draw hand1, hand2
            else
              raise "Invalid choice by #{@player2.class}."
            end
          else
            raise "Invalid choice by #{@player1.class}."
          end
        end
      end
    end
  end

end
